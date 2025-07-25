import React from "react";
import { FaEnvelope, FaInstagram, FaLinkedin } from "react-icons/fa";
import "./Contact.css";

function Contact() {
  return (
    <section className="contact" id="contact">
      <h2>Contact Us</h2>
      <div className="contact-box">
        <p><FaEnvelope /> Email: <a href="mailto:tda.mit@manipal.edu">tda.mit@manipal.edu</a></p>
        <p><FaInstagram /> Instagram: <a href="https://www.instagram.com/tda.manipal/?hl=en">@tda.manipal</a></p>
        <p><FaLinkedin /> LinkedIn: <a href="https://www.linkedin.com/company/the-data-alchemists/?originalSubdomain=in">The Data Alchemists</a></p>
      </div>
    </section>
  );
}

export default Contact;
