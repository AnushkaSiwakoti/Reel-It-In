🎬 Reel It In
Welcome to Reel It In, the AI-powered movie recommendation app that matches your vibe with the perfect films. Whether you're in the mood for a chaotic thriller, a cozy romcom, or something totally out there, just tell us the vibe and we’ll reel in 5 movies, complete with trailers and quirky, human-written descriptions. 🍿

🧠 What It Does
🔍 Smart vibe matching — Type in any mood, genre combo, or chaotic sentence.

🎞 Trailer previews — Click on a poster to play the YouTube trailer instantly.

📝 Unique descriptions — Each movie comes with a short, fun, one-of-a-kind summary written using generative AI.

🎨 Fruity loading screen — Enjoy bouncing blueberries, raspberries, peaches, and lettuce while we work our magic.

💻 Tech Stack
Frontend
React
Custom CSS (no frameworks)
Emoji-powered UI
Animated loader built from fruit images 🍇🍑🥬

Backend
Flask (Python)
OpenAI-compatible API via Together AI
TMDb API for movie data and posters


🚀 Getting Started


Backend Setup
Clone the repo & navigate:

git clone https://github.com/yourusername/reel-it-in.git
cd reel-it-in/backend

Create a virtual environment:

python -m venv venv
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Create a .env file:

TOGETHER_API_KEY=your_together_api_key
TMDB_API_KEY=your_tmdb_api_key
Run the Flask server:


python app.py


Frontend Setup
Navigate to the frontend:

cd ../frontend
Install packages:

npm install
Run the React app:

npm run dev
