import React from "react";
import "./SearchBar.css";

function SearchBar({ vibe, setVibe, onSearch }) {
  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="What's the vibe? e.g., cozy romcom, chaotic thriller..."
        value={vibe}
        onChange={(e) => setVibe(e.target.value)}
      />
      <button onClick={onSearch}>Find My Movie</button>
    </div>
  );
}

export default SearchBar;
