import React from 'react';
import './Blogs.css';
import Navbar from '../Navbar/Navbar';
import Footer from '../Footer/Footer';

function Blogs() {
    return (
        <div className="page-container">
            <div className="content-wrap">
                <Navbar />
                <hr />
                <div className="blogs-container">
                    <h1>My Blog Posts</h1>
                    <div className="blogs-list">
                        <a href="https://medium.com/@vivekdhir77" className="blog-card">
                            <div className="blog-card-content">
                                <h2>My Medium Blog</h2>
                                <p>Check out my technical articles and programming tutorials on Medium. I write about web development, software architecture, and best practices in modern development.</p>
                            </div>
                            <div className="blog-card-image medium-bg"></div>
                        </a>

                        {/* <a href="https://dev.to/vivekdhir77" className="blog-card">
                            <div className="blog-card-content">
                                <h2>Dev.to Articles</h2>
                                <p>Read my posts about web development, algorithms and software engineering. Join the discussion with other developers and share your thoughts on the latest tech trends.</p>
                            </div>
                            <div className="blog-card-image devto-bg"></div>
                        </a> */}

                        {/* <a href="https://hashnode.com/@vivekdhir77" className="blog-card">
                            <div className="blog-card-content">
                                <h2>Hashnode Blog</h2>
                                <p>Follow my developer journey and coding experiences on Hashnode. Discover in-depth tutorials and personal insights into the world of software development.</p>
                            </div>
                            <div className="blog-card-image hashnode-bg"></div>
                        </a> */}
                    </div>
                </div>
            </div>
            <Footer />
        </div>
    );
}

export default Blogs;