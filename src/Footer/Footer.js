import React from 'react';
import './Footer.css'; // Optional: Create a separate CSS file for Footer styles

function Footer() {
    return (
        <div className="Footer">
            <div id="Copyright">
                Copyright © 2024 VIVEK DHIR  
            </div>
            <div className="Socials">
                <div><a href="https://github.com/vivekdhir77/" target="_blank" rel="noopener noreferrer"><img src={`${process.env.PUBLIC_URL}/Icons/github.svg`} alt="Github" /></a></div>
                <div><a href="https://linkedin.com/in/vivekdhir77/" target="_blank" rel="noopener noreferrer"><img src={`${process.env.PUBLIC_URL}/Icons/linkedin.svg`} alt="Linkedin" /></a></div>
                <div><a href="https://instagram.com/vivekdhir77/" target="_blank" rel="noopener noreferrer"><img src={`${process.env.PUBLIC_URL}/Icons/instagram.svg`} alt="instagram" /></a></div>
                <div><a href="https://twitter.com/vivekdhir77/" target="_blank" rel="noopener noreferrer"><img src={`${process.env.PUBLIC_URL}/Icons/twitter.svg`} alt="Twitter" /></a></div>
                <div><a href="mailto:vivekdhir77@gmail.com" target="_blank" rel="noopener noreferrer"><img src={`${process.env.PUBLIC_URL}/Icons/email.svg`} alt="Email" /></a></div>
            </div>
        </div>
    );
}

export default Footer; 