import React from 'react';
import './Resume.css';
import Navbar from '../Navbar/Navbar';
import Footer from '../Footer/Footer';

function Resume() {
    // Get the base URL depending on the environment

    // Use relative path for local development
    const pdfUrl = `${process.env.PUBLIC_URL}/Resume/Vivek_Dhir_Resume.pdf`


    // Function to handle direct PDF viewing
    const handleViewPDF = () => {
        window.open(pdfUrl, '_blank');
    };

    return (
        <div className="page-container">
            <div className="content-wrap">
                <Navbar />
                <hr />
                <div className="resume-container">
                    <h1>Resume</h1>
                    <div className="resume-content">
                        <div className="resume-viewer-container">
                            <object
                                data={pdfUrl}
                                type="application/pdf"
                                className="resume-viewer"
                            >
                                <div className="fallback-message">
                                    Unable to display PDF file. Please use the buttons below to view or download the resume.
                                </div>
                            </object>
                        </div>
                        <div className="resume-buttons">
                            <button 
                                onClick={handleViewPDF}
                                className="view-button"
                            >
                                View PDF
                            </button>
                            <a 
                                href={pdfUrl}
                                download="Vivek_Dhir_Resume.pdf"
                                className="download-button"
                            >
                                Download Resume
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <Footer />
        </div>
    );
}

export default Resume; 