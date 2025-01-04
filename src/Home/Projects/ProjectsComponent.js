import React from 'react';
import './ProjectsComponent.css';

const ProjectsComponent = ({ projectName, projectDescription, projectLink, media }) => {
  return (
    <div className="project-card">
      <div className="project-info">
        <h3>{projectName}</h3>
        <p>{projectDescription}</p>
        <a href={projectLink} target="_blank" rel="noopener noreferrer">
          <button className="view-project-button">View Project</button>
        </a>
      </div>
      <div className="project-media">
        {media}
      </div>
    </div>
  );
};

export default ProjectsComponent;