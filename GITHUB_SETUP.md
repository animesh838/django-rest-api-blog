# GitHub Repository Setup Guide

This guide will help you connect your local Django project to GitHub and set up continuous deployment.

## 🚀 Quick Setup

### 1. Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click the "+" icon in the top right
3. Select "New repository"
4. Name it: `django-rest-api-blog`
5. Make it **Public** (for free hosting options)
6. **Don't** initialize with README (we already have one)
7. Click "Create repository"

### 2. Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Run these in your terminal:

```bash
# Add the remote repository
git remote add origin https://github.com/YOUR_USERNAME/django-rest-api-blog.git

# Push your code to GitHub
git branch -M main
git push -u origin main
```

### 3. Verify Connection

```bash
# Check remote repository
git remote -v

# Should show:
# origin  https://github.com/YOUR_USERNAME/django-rest-api-blog.git (fetch)
# origin  https://github.com/YOUR_USERNAME/django-rest-api-blog.git (push)
```

## 📁 Repository Structure

Your GitHub repository will contain:

```
django-rest-api-blog/
├── api/                    # API app
│   ├── models.py          # Database models
│   ├── serializers.py     # JSON serialization
│   ├── views.py           # API endpoints
│   └── urls.py            # API routing
├── myproject/             # Django settings
├── templates/             # HTML templates
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment config
├── runtime.txt           # Python version
├── .gitignore           # Git ignore rules
├── README.md            # Project documentation
└── DEPLOYMENT.md        # Deployment guide
```

## 🔄 Git Workflow

### Daily Development

```bash
# Check what files have changed
git status

# Add new files or changes
git add .

# Commit your changes
git commit -m "Add new feature: user authentication"

# Push to GitHub
git push origin main
```

### Working with Branches

```bash
# Create a new feature branch
git checkout -b feature/new-api-endpoint

# Make your changes
# ... edit files ...

# Commit changes
git add .
git commit -m "Add new API endpoint"

# Push the branch
git push origin feature/new-api-endpoint

# Create Pull Request on GitHub
# Then merge and delete branch
```

## 🚀 Deployment Integration

### Railway (Recommended)

1. Go to [Railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Connect your GitHub account
5. Select your repository: `django-rest-api-blog`
6. Railway will automatically detect Django and deploy
7. Add environment variables:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app.railway.app
   ```

### Render

1. Go to [Render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn myproject.wsgi:application`
5. Add environment variables

## 📊 GitHub Features

### Issues
- Track bugs and feature requests
- Assign labels and milestones
- Link issues to pull requests

### Pull Requests
- Review code changes
- Run automated tests
- Merge safely

### Actions (CI/CD)
Create `.github/workflows/django.yml`:

```yaml
name: Django CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.11
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python manage.py test
```

## 🔒 Security Best Practices

### Environment Variables
Never commit sensitive data:
- Database passwords
- API keys
- Secret keys
- Email credentials

### .gitignore
Already configured to exclude:
- `db.sqlite3` (database)
- `venv/` (virtual environment)
- `.env` (environment variables)
- `__pycache__/` (Python cache)

## 📈 Repository Analytics

GitHub provides:
- **Traffic**: Views and clones
- **Contributors**: Who's working on the project
- **Releases**: Version management
- **Insights**: Code frequency and activity

## 🎯 Next Steps

1. **Create GitHub repository** following the steps above
2. **Push your code** to GitHub
3. **Set up deployment** (Railway/Render)
4. **Add collaborators** if working with a team
5. **Create issues** for future features
6. **Set up CI/CD** with GitHub Actions

## 📞 Troubleshooting

### Common Issues

**"Repository not found"**
- Check repository URL
- Verify GitHub permissions
- Ensure repository is public (if using free hosting)

**"Permission denied"**
- Use SSH keys or personal access tokens
- Check GitHub authentication

**"Branch not found"**
- Run `git branch -M main` to rename branch
- Push with `git push -u origin main`

### Useful Commands

```bash
# Check repository status
git status

# View commit history
git log --oneline

# Check remote configuration
git remote -v

# Reset to last commit
git reset --hard HEAD

# View file changes
git diff
```

---

**Your Django project is now ready for GitHub and deployment!** 🎉 