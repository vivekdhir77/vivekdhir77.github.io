import React from 'react';
import './Home.css';
import Navbar from './Navbar';
import Footer from './Footer';

function Home() {
    return (
        <div className="Home">
            <Navbar />
            <hr />
            <div className="About">
                <div className="AboutContent">
                    <img src="./Profile.jpeg" alt="Profile Picture" />
                    <div className="TextContent">
                        <h1>About Me</h1>
                        <h2>Bio:</h2>
                        <p>My interest in math and computers allows me to explore challenges in computer science and interdisciplinary fields that require fast computation and the designing of optimized algorithms.</p>
                        <p>Along with this, I have a keen interest in developing and designing robust softwares.</p>
                        <p>Currently, I am enjoying competitive programming and Machine Learning.</p>
                    </div>
                </div>
            </div>
            <Footer />
        </div>
    );
}

export default Home;