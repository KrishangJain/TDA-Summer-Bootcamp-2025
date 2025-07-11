import { useState } from 'react';

export default function Header() {
  const [langOpen, setLangOpen] = useState(false);

  return (
    <header className="header">
      <img src="/Netflix_logo.svg" alt="Netflix" className="logo" />
      <div className="header-right">
        <div className="language-dropdown" onClick={() => setLangOpen(!langOpen)}>
          🌐 English ▼
          {langOpen && (
            <ul className="dropdown">
              <li>English</li>
              <li>हिन्दी</li>
            </ul>
          )}
        </div>
        <button className="sign-in-btn">Sign In</button>
      </div>
    </header>
  );
}
