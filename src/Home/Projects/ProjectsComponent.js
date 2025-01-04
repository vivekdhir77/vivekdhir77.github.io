import React from 'react';
import './ProjectsComponent.css';

const ProjectsComponent = ({ title, description, link, image }) => {
    return (
        <div className="project-card">
            <img src={image} alt={title} />
            <h2>{title}</h2>
            <p>{description}</p>
            <a href={link} target="_blank" rel="noopener noreferrer">View Project</a>
        </div>
    );
};

export default ProjectsComponent;