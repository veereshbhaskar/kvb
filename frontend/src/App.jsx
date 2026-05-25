import { useMemo, useState } from 'react'

const skills = [
  'React.js',
  'JavaScript / ES6+',
  'Responsive UI',
  'Flask / Python',
  'SQLite',
  'REST APIs',
]

const projects = [
  {
    title: 'Portfolio Website',
    description: 'A fast React portfolio with a polished modern layout and backend contact form.',
    link: 'https://veereshbhaskar.github.io/kvb',
  },
  {
    title: 'Project Manager',
    description: 'An admin-style dashboard concept for managing content and messages.',
    link: 'https://github.com/veereshbhaskar/kvb',
  },
]

const features = [
  'Custom React experience with glassmorphism',
  'Backend contact API saved to SQLite',
  'Clean, responsive design for recruiters',
]

function App() {
  const [form, setForm] = useState({ name: '', email: '', message: '' })
  const [status, setStatus] = useState(null)

  const handleChange = (event) => {
    const { name, value } = event.target
    setForm((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setStatus({ type: 'loading', message: 'Sending message...' })

    try {
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      })

      const data = await response.json()
      if (!response.ok) throw new Error(data.error || 'Could not send message')

      setStatus({ type: 'success', message: data.message || 'Message sent!' })
      setForm({ name: '', email: '', message: '' })
    } catch (error) {
      setStatus({ type: 'error', message: error.message })
    }
  }

  const details = useMemo(
    () => [
      { label: 'Location', value: 'Remote / India' },
      { label: 'Role', value: 'Full-stack Developer' },
      { label: 'Tech', value: 'React + Flask' },
    ],
    []
  )

  return (
    <div className="app-shell">
      <div className="page-background">
        <div className="background-ring ring-left" />
        <div className="background-ring ring-right" />
      </div>

      <header className="hero-section">
        <div className="hero-copy">
          <p className="eyebrow">Designer & Developer</p>
          <h1>Hi, I’m Veeresh.</h1>
          <p className="tagline">
            I create modern web portfolios that impress recruiters with clean UX, polished visuals, and fast backend performance.
          </p>

          <div className="hero-badges">
            {features.map((feature) => (
              <span key={feature} className="badge">
                {feature}
              </span>
            ))}
          </div>

          <div className="hero-actions">
            <a className="button button-primary" href="#projects">
              See Work
            </a>
            <a className="button button-secondary" href="#contact">
              Hire Me
            </a>
          </div>
        </div>

        <div className="hero-panel">
          <div className="panel-card">
            <h2>About this portfolio</h2>
            <p>
              A polished full-stack demo using React for the interface and Flask for a contact API. It is built to look premium and feel smooth on every screen.
            </p>

            <ul>
              {details.map((item) => (
                <li key={item.label}>
                  <strong>{item.value}</strong>
                  <span>{item.label}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </header>

      <main>
        <section id="about" className="section-card section-highlight">
          <div className="section-header">
            <h2>Why choose this project?</h2>
            <p>This portfolio is designed to present your skills with a strong visual impression and a polished digital resume.</p>
          </div>
          <div className="feature-grid">
            <article>
              <h3>Modern Design</h3>
              <p>Glassmorphism, gradients, and bold typography that feel premium and professional.</p>
            </article>
            <article>
              <h3>Fast Experience</h3>
              <p>React keeps interactions smooth, while Flask handles form submissions with a real backend.</p>
            </article>
            <article>
              <h3>Recruiter-ready</h3>
              <p>Clear sections, strong calls to action, and a contact form that encourages outreach.</p>
            </article>
          </div>
        </section>

        <section id="skills" className="section-card">
          <div className="section-header">
            <h2>Skills</h2>
            <p>Core technologies and strengths I bring to your next web project.</p>
          </div>
          <div className="skill-grid">
            {skills.map((skill) => (
              <div key={skill} className="skill-pill">
                {skill}
              </div>
            ))}
          </div>
        </section>

        <section id="projects" className="section-card">
          <div className="section-header">
            <h2>Highlighted projects</h2>
            <p>Live examples and repo links that showcase work quality and technical skill.</p>
          </div>
          <div className="project-grid">
            {projects.map((project) => (
              <article key={project.title} className="project-card">
                <h3>{project.title}</h3>
                <p>{project.description}</p>
                <a target="_blank" rel="noreferrer" href={project.link}>
                  Open project
                </a>
              </article>
            ))}
          </div>
        </section>

        <section id="contact" className="section-card contact-card">
          <div className="contact-copy">
            <span className="eyebrow">Let’s connect</span>
            <h2>Contact me for your next web project</h2>
            <p>Submit your message through the live backend form and I’ll respond quickly.</p>
          </div>

          <form onSubmit={handleSubmit} className="contact-form">
            <label>
              Preferred Name
              <input
                name="name"
                value={form.name}
                onChange={handleChange}
                placeholder="Preferred Name"
                required
              />
            </label>
            <label>
              Email address
              <input
                type="email"
                name="email"
                value={form.email}
                onChange={handleChange}
                placeholder="you@example.com"
                required
              />
            </label>
            <label>
              Message
              <textarea
                name="message"
                value={form.message}
                onChange={handleChange}
                placeholder="Hi Veeresh, I’d like to discuss a project..."
                rows="5"
                required
              />
            </label>
            <button type="submit" className="button button-primary">
              Send Message
            </button>
            {status && (
              <p className={`status-message ${status.type}`}>{status.message}</p>
            )}
          </form>
        </section>
      </main>

      <footer className="footer-bar">
        <div>
          <strong>Veeresh Bhaskar</strong>
          <span>React + Flask portfolio</span>
        </div>
        <div className="social-links">
          <a href="https://github.com/veereshbhaskar" target="_blank" rel="noreferrer">
            GitHub
          </a>
          <a href="https://linkedin.com" target="_blank" rel="noreferrer">
            LinkedIn
          </a>
        </div>
      </footer>
    </div>
  )
}

export default App
