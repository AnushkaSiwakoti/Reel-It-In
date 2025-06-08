import React from "react";
import "./Loader.css";

function Loader() {
  return (
    <div className="loader-overlay">
      <div className="fruit-blobs">
        <img src="/raspberry.png" alt="raspberry" className="fruit" />
        <img src="/peach.png" alt="peach" className="fruit" />
        <img src="/blueberry.png" alt="blueberry" className="fruit" />
        <img src="/lettuce.png" alt="lettuce" className="fruit" />
      </div>
      <div className="loader-text">Loading movie magic... ✨</div>
    </div>
  );
}

export default Loader;
