import React from "react";
import "./Hero.css";

function Hero() {
  return (
    <section className="hero" id="hero">
      <div className="hero-content">
        <h1>Welcome to <span className="highlight">The Data Alchemists</span></h1>
        <p>Your gateway into the world of Data Science, Machine Learning, and AI.</p>
        <a href="#about" className="hero-btn">Learn More ↓</a>
      </div>
    </section>
  );
}

export default Hero;
