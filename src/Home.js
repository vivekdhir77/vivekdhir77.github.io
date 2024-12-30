import React from 'react';
import './Home.css';
import Navbar from './Navbar/Navbar';
import Footer from './Footer/Footer';
import About from './Home/About';

function Home() {
    return (
        <div className="Home">
            <Navbar />
            <hr />
            <About />
            <Footer />
        </div>
    );
}

export default Home;