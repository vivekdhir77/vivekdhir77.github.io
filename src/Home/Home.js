import React from 'react';
import './Home.css';
import Navbar from '../Navbar/Navbar';
import Footer from '../Footer/Footer';
import About from './About';

function Home() {
    return (
        <div className="page-container">
            <Navbar />
            <hr />
            <div className="content-wrap">
                <About/>
            </div>
            <Footer />
        </div>
    );
}

export default Home;
