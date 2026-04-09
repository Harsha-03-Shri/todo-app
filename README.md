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

### Option 1: Using Vercel Dashboard (Recommended)

1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Add todo app"
   git push
   ```

2. Go to [vercel.com](https://vercel.com) and import your repository

3. Vercel will automatically detect the configuration from `vercel.json`

4. Click "Deploy" - that's it!

### Option 2: Using Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy from project root
cd /home/shriharsha/Code/CAIT/todo-app
vercel --prod
```

### Important Notes

- The `vercel.json` is configured to:
  - Build the React frontend automatically
  - Serve the frontend from `/`
  - Route API requests from `/api/*` to the FastAPI backend
- No need to manually build or move files
- The API uses in-memory storage, so todos reset on each deployment

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
