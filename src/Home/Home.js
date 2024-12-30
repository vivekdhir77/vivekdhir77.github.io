import React from 'react';
import './Home.css';
import Navbar from '../Navbar/Navbar';
import Footer from '../Footer/Footer';
import About from './About';
import Experience from './Experience/Experience';
import Projects from './Projects/Projects';

function Home() {
    return (
        <div className="page-container">
            <Navbar />
            <hr />
            <div className="content-wrap">
                <About/>
                <Experience/>
                <Projects/>
            </div>
            <Footer />
        </div>
    );
}

export default Home;
