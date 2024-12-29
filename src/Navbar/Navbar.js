import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const location = useLocation();

    const toggleMenu = () => {
        setIsMenuOpen(!isMenuOpen);
    };

    return (
        <nav className="Navbar">
            <div className="Navbar_mediaq">
                <div id="Name">VIVEK DHIR</div>
                <div className="Hamburger" onClick={toggleMenu}>
                    <img src="/Icons/menu.png" alt="Hamburger Menu" />
                </div>
            </div>
            <div className={`Headings ${isMenuOpen ? 'show' : ''}`}>
                <Link to="/" className={location.pathname === '/' ? 'active' : ''}>
                    <div>About</div>
                </Link>
                <Link to="/blogs" className={location.pathname === '/blogs' ? 'active' : ''}>
                    <div>Blogs</div>
                </Link>
                <Link to="/resume" className={location.pathname === '/resume' ? 'active' : ''}>
                    <div>Resume</div>
                </Link>
            </div>
        </nav>
    );
}

export default Navbar; 