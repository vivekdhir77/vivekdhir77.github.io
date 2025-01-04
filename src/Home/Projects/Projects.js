import React from 'react';
import ProjectsComponent from './ProjectsComponent';
import './Projects.css';

const Projects = () => {
    return (
        <div className="projects-container">
            <h1>Projects</h1>
            <div className="projects-grid">
                <ProjectsComponent
                    title="Project Title 1"
                    description="Brief description of Project 1."
                    link="https://link-to-project1.com"
                    image="path/to/image1.png"
                />
                <ProjectsComponent
                    title="Project Title 2"
                    description="Brief description of Project 2."
                    link="https://link-to-project2.com"
                    image="path/to/image2.png"
                />
                {/* Add more projects as needed */}
            </div>
        </div>
    );
};

export default Projects;
