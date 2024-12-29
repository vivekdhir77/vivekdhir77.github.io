import React from 'react';
import './Home.css';

function About() {
    return (
        <div className="About">
            <div className="AboutContent">
                <img src={`${process.env.PUBLIC_URL}/Profile.jpeg`} alt="Profile Picture" />
                <div className="TextContent">
                    <h1>About</h1>
                    <p>My interest in math and computers allows me to explore challenges in computer science and interdisciplinary fields that require fast computation and the designing of optimized algorithms.</p>
                    <p>Along with this, I have a keen interest in developing and designing robust softwares.</p>
                    <p>Currently, I am enjoying competitive programming and Machine Learning.</p>
                </div>
            </div>
        </div>
    );
}

export default About;