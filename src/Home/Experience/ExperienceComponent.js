import React from 'react';
import './ExperienceComponent.css';

const ExperienceComponent = ({
  companyName,
  position,
  startDate,
  endDate,
  description,
  companyLogo,
  companyLink
}) => {
  return (
    <a href={companyLink} target="_blank" rel="noopener noreferrer" style={{ textDecoration: 'none' }}>
        <div className="experience-card">
        <div className="experience-text">
            <h2 className="position">{position}</h2>
            <h3 className="company">{companyName}</h3>
            <div className="date-range">
            {startDate} - {endDate}
            </div>
            <p className="description">{description}</p>
        </div>
        <div className="experience-logo">
            <img src={`${process.env.PUBLIC_URL}/${companyLogo}`} alt={`${companyName} logo`} />
        </div>
        </div>
    </a>
  );
};

export default ExperienceComponent;