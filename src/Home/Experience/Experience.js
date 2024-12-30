import React from 'react';
import './ExperienceComponent.css';
import ExperienceComponent from './ExperienceComponent';

const Experience = () => {
  return (
    <div className="experience-container">
      <h1>Experience</h1>
      <div className="experience-grid">
        <ExperienceComponent
        companyName="Augmented Cognition Laboratory (Northeastern University, Boston)"
        position="Computer Vision Researcher"
        startDate="Sept 2024"
        endDate="Present"
        description={
            <>
            <p>Working towards developing a joint frame-pose embedding model integrating 6D camera pose data and video frames to ensure temporally consistent, spatially accurate driving scene generation for autonomous systems. Working under Dr. Sarah Ostadabbas.</p>
            </>
        }
        companyLogo="ACLab.jpg"
        companyLink="https://ostadabbas.sites.northeastern.edu/"
        />
        <ExperienceComponent
        companyName="One AI Click"
        position="Founder"
        startDate="Aug 2024"
        endDate="Aug 2024"
        description={
            <>
            <p>• Founded One AI Click to develop a tool aimed at simplifying the fine-tuning process for large language models (LLMs).</p>
            <p>• Conducted extensive research and development to create a user-friendly interface and efficient backend for the tool.</p>
            <p>• Collaborated with a team of engineers (<a href="https://www.linkedin.com/in/sai-srikar-ventrapragada/">Srikar</a> <a href="https://www.linkedin.com/in/sai-ravi-teja-gangavarapu/">Ravi</a>) to implement cutting-edge techniques in LLM fine-tuning.</p>
            <p>• Successfully launched a beta version.</p>
            </>
        }
        companyLogo="Click.png"
        companyLink="https://oneaiclick.com"
        />
        <ExperienceComponent
        companyName="Aiden AI"
        position="Software Engineer Intern"
        startDate="Jan 2024"
        endDate="July 2024"
        description={
            <>
            <p>• Optimized language model deployment, reducing size by 20% with quantization techniques while maintaining 90% performance.</p>
            <p>• Enhanced model specificity using fine-tuning and synthetic data generation.</p>
            <p>• Developed a knowledge management system with RAG and corrective agents.</p>
            <p>• Created a usability rating system using user interaction data for better UX insights.</p>
            <p>• Automated meeting minutes and implemented a chatbot for post-meeting insights.</p>
            <p>• Built a Python orchestration solution to optimize workflows.</p>
            <p>• Proposed an automated server deployment solution with Python and AWS SDK, improving efficiency.</p>
            </>
        }
        companyLogo="AidenAI.png"
        companyLink="https://aidenai.com"
        />
        <ExperienceComponent
          companyName="Oracle"
          position="Intern"
          startDate="June 2023"
          endDate="August 2023"
          description={
            <>
              <p>• Enhanced bancassurance project by designing UI/UX in Figma and developing backend with Spring Boot.</p>
              <p>• Implemented frontend in Angular to build data visualizations, improving decision-making efficiency and customer satisfaction.</p>
              <p>• Made an animation video to explain oracle bancassurance.</p>
              <p>• Additionally, streamlined document templates and improved documentation organization.</p>
            </>
          }
          companyLogo="Oracle.png"
          companyLink="https://www.oracle.com/financial-services/"
        />
      </div>
    </div>
  );
};

export default Experience;
