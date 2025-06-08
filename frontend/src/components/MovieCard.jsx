import React, { useState } from "react";
import "./MovieCard.css";

function MovieCard({ movie }) {
  const [showTrailer, setShowTrailer] = useState(false);

  const handlePosterClick = () => {
    setShowTrailer(!showTrailer);
  };

  return (
    <div className="movie-card">
      <div className="poster-side" onClick={handlePosterClick}>
        <img className="poster-image" src={movie.poster} alt={movie.title} />
        <div className="click-overlay">▶ Watch Trailer</div>
      </div>
      <div className="info-side">
        <h2 className="movie-title">{movie.title}</h2>
        <p className="movie-description">{movie.description}</p>
        {showTrailer && movie.trailer && (
          <div className="trailer-wrapper">
            <iframe
              src={`https://www.youtube.com/embed/${movie.trailer}?autoplay=1`}
              title="Movie trailer"
              frameBorder="0"
              allow="autoplay; encrypted-media"
              allowFullScreen
            />
          </div>
        )}
      </div>
    </div>
  );
}

export default MovieCard;
