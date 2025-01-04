import React from 'react';
import './Projects.css';
import ProjectsComponent from './ProjectsComponent';

const Projects = () => {
  return (
    <div className="projects-container">
      <hr />
      <div className="projects-grid">
        <ProjectsComponent
          projectName="One AI Click"
          projectDescription="LLM fine-tuning abstraction tool"
          projectLink="https://oneaiclick.com"
          media={
            <div className="video-container">
              <iframe
                src="https://www.youtube.com/embed/zHRR3NSMXcU"
                title="YouTube video player"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              ></iframe>
            </div>
          }
        />
        <hr />
        <ProjectsComponent
          projectName="Prime Plot"
          projectDescription="Empowering Business Owners with Data-Driven Location Choices (HackUmass 2024) (https://devpost.com/software/prime-plot)"
          projectLink="https://prime-plot.vercel.app/"
          media={
            <img
              src={`${process.env.PUBLIC_URL}/PrimePlot.png`}
              alt="Project Media"
              width="480"
              height="300"
            />
          }
        />
        <hr />
        <ProjectsComponent
          projectName="AI Car"
          projectDescription="Self driving car simulation using pygame and neural network from ground up."
          projectLink="https://github.com/vivekdhir77/AI-Car"
          media={
            <img
              src={`${process.env.PUBLIC_URL}/AICar.png`}
              alt="Project Media"
              width="480"
              height="300"
            />
          }
        />
      </div>
    </div>
  );
};

export default Projects;
