import React, { useState } from "react";
import SearchBar from "./components/SearchBar";
import MovieCard from "./components/MovieCard";
import Loader from "./components/Loader";
import "./App.css";

function App() {
  const [vibe, setVibe] = useState("");
  const [movies, setMovies] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!vibe) return;
    setLoading(true);
    setMovies([]);

    try {
      const response = await fetch("http://127.0.0.1:5000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ vibe }),
      });

      if (!response.ok) throw new Error("Failed to fetch movies");

      const data = await response.json();
      setMovies(data); // expects array of movies
    } catch (err) {
      console.error("Error fetching movies:", err);
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <h1>🎬 Reel It In</h1>
      <SearchBar vibe={vibe} setVibe={setVibe} onSearch={handleSearch} />
      {loading && <Loader />}
      <div className="movie-list">
        {movies.map((movie, index) => (
          <MovieCard key={index} movie={movie} />
        ))}
      </div>
    </div>
  );
}

export default App;
