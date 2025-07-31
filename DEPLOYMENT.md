# Deployment Guide

This guide will help you deploy your Django REST Framework application to various hosting platforms.

## 🚀 Quick Deploy Options

### 1. Railway (Recommended - Easiest)

**Steps:**
1. Push your code to GitHub
2. Go to [Railway.app](https://railway.app)
3. Connect your GitHub repository
4. Railway will automatically detect Django and deploy
5. Add environment variables:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.railway.app
   ```

**Benefits:**
- Free tier available
- Automatic HTTPS
- Easy database setup
- Automatic deployments

### 2. Render

**Steps:**
1. Push code to GitHub
2. Go to [Render.com](https://render.com)
3. Create new Web Service
4. Connect your repository
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `gunicorn myproject.wsgi:application`
7. Add environment variables

### 3. PythonAnywhere

**Steps:**
1. Create account at [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Upload your code or clone from GitHub
3. Create virtual environment
4. Install requirements: `pip install -r requirements.txt`
5. Configure WSGI file
6. Set up static files

## 🔧 Pre-Deployment Checklist

### 1. Update Settings for Production

Your `settings.py` is already configured for production with:
- Environment variable support
- Security headers
- Static file configuration
- CORS settings

### 2. Environment Variables

Create these environment variables on your hosting platform:

```bash
SECRET_KEY=your-very-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com,your-app-name.railway.app
```

### 3. Database Setup

**For SQLite (Development):**
- Already configured
- Works for small applications

**For PostgreSQL (Production):**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

### 4. Static Files

Run this command after deployment:
```bash
python manage.py collectstatic
```

## 📁 Files Added for Deployment

- `Procfile` - Tells hosting platforms how to run your app
- `runtime.txt` - Specifies Python version
- `requirements.txt` - Updated with gunicorn
- `DEPLOYMENT.md` - This guide

## 🌐 Domain Configuration

### Custom Domain
1. Buy a domain (Namecheap, GoDaddy, etc.)
2. Point DNS to your hosting provider
3. Configure SSL certificate

### Subdomain
Most platforms provide free subdomains like:
- `your-app.railway.app`
- `your-app.onrender.com`
- `your-app.pythonanywhere.com`

## 🔒 Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Enable HTTPS
- [ ] Set up proper CORS settings
- [ ] Use environment variables for secrets

## 📊 Monitoring

### Railway
- Built-in logs and monitoring
- Automatic restarts on crashes
- Performance metrics

### Render
- Request logs
- Build logs
- Health checks

### PythonAnywhere
- Error logs
- Access logs
- Resource usage

## 🚨 Troubleshooting

### Common Issues

1. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check `STATIC_ROOT` configuration

2. **Database errors**
   - Run migrations: `python manage.py migrate`
   - Check database connection

3. **CORS errors**
   - Update `CORS_ALLOWED_ORIGINS` with your domain
   - Check frontend URL configuration

4. **500 errors**
   - Check logs for specific error messages
   - Verify environment variables are set

### Debug Commands

```bash
# Check if app can start
python manage.py check --deploy

# Test database connection
python manage.py dbshell

# Check static files
python manage.py collectstatic --dry-run
```

## 💰 Cost Comparison

| Platform | Free Tier | Paid Plans | Ease of Use |
|----------|-----------|------------|-------------|
| Railway | ✅ | $5/month | ⭐⭐⭐⭐⭐ |
| Render | ✅ | $7/month | ⭐⭐⭐⭐ |
| PythonAnywhere | ✅ | $5/month | ⭐⭐⭐ |
| Heroku | ❌ | $7/month | ⭐⭐⭐⭐ |
| DigitalOcean | ❌ | $6/month | ⭐⭐ |

## 🎯 Recommended for Beginners

**Railway** is the best choice because:
- Free tier available
- Automatic deployments
- Built-in database support
- Excellent documentation
- Great developer experience

## 📞 Support

If you encounter issues:
1. Check the platform's documentation
2. Look at deployment logs
3. Test locally with production settings
4. Ask in platform-specific communities

---

**Next Steps:**
1. Choose a hosting platform
2. Follow the platform-specific guide
3. Deploy your application
4. Test all functionality
5. Set up monitoring and alerts 