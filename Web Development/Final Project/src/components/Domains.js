import React from "react";
import "./Domains.css";

function Domains() {
  const domainList = [
    "Artificial Intelligence & Machine Learning",
    "Data Analytics & Visualization",
    "Deep Learning",
    "Coding & Development",
    "HR & Management",
    "PR & Outreach",
  ];

  return (
    <section className="domains" id="domains">
      <h2>Our Domains</h2>
      <div className="domain-cards">
        {domainList.map((domain, i) => (
          <div key={i} className="card">
            <h3>{domain}</h3>
            <p>Explore the fascinating world of {domain.toLowerCase()}.</p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Domains;
