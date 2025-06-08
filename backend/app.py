from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests
import random

# Load environment variables
load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

print("Together AI key loaded:", bool(TOGETHER_API_KEY))
print("TMDB key loaded:", bool(TMDB_API_KEY))

app = Flask(__name__)
CORS(app)

def get_gpt_response(prompt):
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are NOT allowed to reuse sentence structures, tone, or adjectives across completions. "
                    "Avoid clichés like 'charming', 'heartwarming', 'get ready to swoon', 'iconic', or 'sweet'. "
                    "Your goal is to make each description feel *totally fresh*, unique, and emotionally in tune with the requested vibe."
                    "keep the length to about 3 sentences."
                    "Just give the description nothing extra"
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 1.2,
        "max_tokens": 400,
        "top_p": 0.95
    }

    response = requests.post("https://api.together.ai/v1/chat/completions", headers=headers, json=payload)
    if response.status_code != 200:
        print("Together AI ERROR:", response.status_code, response.text)
        response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def build_description_prompt(title, vibe):
    templates = [

        f"Describe the movie '{title}' in 2-3 short sentences so that someone who’s in the mood for a '{vibe}' movie will want to watch it. "
        f"Explain what it's about in a way that’s natural, vivid, and human — like you’re telling a friend what makes it interesting. "
        f"Do not repeat phrasing from previous descriptions. Be specific, avoid generic words like 'great', 'iconic', or 'emotional'."
    ]
    return random.choice(templates)

@app.route("/recommend", methods=["POST"])
def recommend_movie():
    try:
        data = request.get_json()
        vibe = data.get("vibe", "")
        if not vibe:
            return jsonify({"error": "No vibe provided"}), 400

        # Ask Together AI for 5 movie titles
        prompt = f"Suggest five movies that match this vibe: '{vibe}'. Return only the movie titles in a comma-separated list."
        titles_response = get_gpt_response(prompt)
        print("Suggested titles:", titles_response)

        # Parse movie titles
        titles = [title.strip() for title in titles_response.split(",") if title.strip()]
        print("Parsed titles:", titles)

        movies_data = []

        for title in titles:
            # Search TMDb
            search_url = f"https://api.themoviedb.org/3/search/movie?query={title}&api_key={TMDB_API_KEY}"
            search_res = requests.get(search_url).json()
            results = search_res.get("results", [])
            if not results:
                continue

            movie = results[0]
            movie_id = movie.get("id")
            poster_path = movie.get("poster_path", "")
            trailer_key = ""

            # Get trailer
            try:
                videos_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}"
                videos_res = requests.get(videos_url).json()
                for vid in videos_res.get("results", []):
                    if vid["type"] == "Trailer" and vid["site"] == "YouTube":
                        trailer_key = vid["key"]
                        break
            except Exception as e:
                print("Trailer error:", e)

            # Get fun, human description
            try:
                desc_prompt = build_description_prompt(title, vibe)
                description = get_gpt_response(desc_prompt)
            except Exception as e:
                print("Description error:", e)
                description = "No description available."

            movies_data.append({
                "title": title,
                "poster": f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "",
                "trailer": trailer_key,
                "description": description
            })

        return jsonify(movies_data)

    except Exception as e:
        print("MAIN ROUTE ERROR:", str(e))
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
