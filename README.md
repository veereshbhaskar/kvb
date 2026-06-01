
# Veeresh Bhaskar Portfolio

A modern full-stack portfolio website built with React and Flask. The project presents skills, highlighted work, and a contact form backed by a small SQLite database.

## Live Site

Visit the portfolio on GitHub Pages:

https://veereshbhaskar.github.io/kvb/

## What This Project Includes

- Responsive React frontend built with Vite
- Flask backend API for contact form submissions
- SQLite database for storing contact messages
- GitHub Actions workflow for build validation
- Render deployment configuration for the backend
- Dockerfile for container-based deployment

## Project Structure

```text
.
├── app.py                  # Flask backend and API routes
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment config
├── Dockerfile              # Docker deployment setup
├── frontend/               # React + Vite frontend
│   ├── src/
│   ├── package.json
│   └── vite.config.js
└── tests/                  # Backend regression tests
```

## Running Locally

Install and build the frontend:

```bash
cd frontend
npm install
npm run build
```

Install backend dependencies and start Flask:

```bash
cd ..
pip install -r requirements.txt
python app.py
```

Open the app at:

```text
http://localhost:5000
```

## Running Tests

```bash
python -m unittest discover -s tests
```

## Deployment Notes

GitHub Pages can host the static React frontend, but it cannot run the Flask backend. Because of that, the contact form needs a deployed backend URL, such as the Render service, to save messages successfully.

Render can run the full Flask app and serve the built frontend from `frontend/dist`.

## API Endpoints

```text
POST /api/contact
```

Saves a contact message. Required fields:

- `name`
- `email`
- `message`

```text
GET /api/messages
```

Returns saved contact messages.

```text
POST /api/messages/clear
```

Clears saved messages.

## Tech Stack

- React
- Vite
- Flask
- SQLite
