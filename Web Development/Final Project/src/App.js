import React from "react";
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import About from './components/About';
import Domains from './components/Domains';
import Contact from './components/Contact';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Hero />
      <About />
      <Domains />
      <Contact />
    </div>
  );
}

export default App;
