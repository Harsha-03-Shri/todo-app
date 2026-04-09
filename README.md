# Todo List App

A minimal todo list application built with FastAPI and React, deployable on Vercel.

## Features

- ✅ Add, complete, and delete todos
- 🎨 Modern, responsive UI
- 🚀 FastAPI backend as serverless functions
- ⚡ React frontend with hooks

## Local Development

### Backend (FastAPI)

```bash
# Install dependencies
pip install -r api/requirements.txt

# Run the server
uvicorn api.index:app --reload --port 8000
```

### Frontend (React)

```bash
cd frontend
npm install
npm start
```

The app will run on `http://localhost:3000` and proxy API requests to `http://localhost:8000`.

## Deploy to Vercel

### Option 1: Using Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Build frontend
cd frontend && npm run build && cd ..

# Move build to root
mv frontend/build ./public

# Deploy
vercel --prod
```

### Option 2: Using Vercel Dashboard

1. Push your code to GitHub
2. Import the repository in Vercel
3. Set build settings:
   - Build Command: `cd frontend && npm install && npm run build && cd .. && mv frontend/build ./public`
   - Output Directory: `public`
4. Deploy!

### Environment Variables (Production)

For production, set `REACT_APP_API_URL` to your Vercel deployment URL:
- `REACT_APP_API_URL=https://your-app.vercel.app/api`

## Project Structure

```
todo-app/
├── api/
│   ├── index.py          # FastAPI backend
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── App.js       # Main React component
│   │   └── App.css      # Styles
│   └── package.json     # Node dependencies
└── vercel.json          # Vercel configuration
```

## API Endpoints

- `GET /api/todos` - Get all todos
- `POST /api/todos` - Create a new todo
- `PUT /api/todos/{id}` - Update a todo
- `DELETE /api/todos/{id}` - Delete a todo

## Notes

- The backend uses in-memory storage, so todos will reset on each deployment
- For persistent storage, consider adding a database (PostgreSQL, MongoDB, etc.)
