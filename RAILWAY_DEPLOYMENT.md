# Railway Deployment Guide

This guide will help you deploy your Django REST Framework application to Railway.

## 🚀 Quick Deploy to Railway

### Step 1: Create Railway Account

1. Go to [Railway.app](https://railway.app)
2. Click "Start a New Project"
3. Sign up with your GitHub account (recommended)

### Step 2: Deploy from GitHub

1. **Connect GitHub**:
   - Click "Deploy from GitHub repo"
   - Authorize Railway to access your GitHub account
   - Select your repository: `animesh838/django-rest-api-blog`

2. **Railway will automatically**:
   - Detect Django framework
   - Install dependencies from `requirements.txt`
   - Run database migrations
   - Start the server with gunicorn

### Step 3: Configure Environment Variables

**Add these environment variables in Railway dashboard:**

1. Go to your project in Railway
2. Click "Variables" tab
3. Add these variables:

```bash
SECRET_KEY=26)d=z^*44_^%jg2bfmgkq1y4jdrj2*qmaoxt@kz&2(t)z^e^)
DEBUG=False
ALLOWED_HOSTS=your-app-name.railway.app
```

**Replace `your-app-name.railway.app` with your actual Railway domain.**

### Step 4: Database Setup

Railway will automatically:
- Create a PostgreSQL database
- Run `python manage.py migrate`
- Set up database connection

### Step 5: Post-Deployment Setup

After deployment, run these commands in Railway terminal:

```bash
# Create superuser (optional)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

## 🔧 Railway Configuration

### Automatic Detection
Railway automatically detects:
- **Framework**: Django
- **Python version**: 3.11 (from `runtime.txt`)
- **Start command**: `gunicorn myproject.wsgi:application` (from `Procfile`)

### Build Process
1. Install dependencies: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Collect static files: `python manage.py collectstatic --noinput`
4. Start server: `gunicorn myproject.wsgi:application`

## 🌐 Access Your Application

### URLs
- **Main site**: `https://your-app-name.railway.app/`
- **Posts page**: `https://your-app-name.railway.app/posts/`
- **Admin panel**: `https://your-app-name.railway.app/admin/`
- **API root**: `https://your-app-name.railway.app/api/`

### API Endpoints
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create new post
- `GET /api/posts/{id}/` - Get specific post
- `PUT /api/posts/{id}/` - Update post
- `DELETE /api/posts/{id}/` - Delete post

## 📊 Railway Features

### Monitoring
- **Logs**: Real-time application logs
- **Metrics**: CPU, memory, and network usage
- **Health checks**: Automatic restart on crashes

### Database
- **PostgreSQL**: Managed database
- **Automatic backups**: Daily backups
- **Connection pooling**: Optimized performance

### Scaling
- **Auto-scaling**: Based on traffic
- **Custom domains**: Add your own domain
- **SSL certificates**: Automatic HTTPS

## 🔒 Security

### Environment Variables
- **SECRET_KEY**: Django secret key
- **DEBUG**: Set to False in production
- **ALLOWED_HOSTS**: Your Railway domain

### HTTPS
- Automatic SSL certificates
- Secure by default

## 🚨 Troubleshooting

### Common Issues

**1. Build Failures**
```bash
# Check logs in Railway dashboard
# Common causes:
# - Missing dependencies in requirements.txt
# - Python version mismatch
# - Database connection issues
```

**2. 500 Errors**
```bash
# Check environment variables
# Verify SECRET_KEY is set
# Check ALLOWED_HOSTS includes your domain
```

**3. Database Errors**
```bash
# Run migrations manually
python manage.py migrate

# Check database connection
python manage.py dbshell
```

**4. Static Files Not Loading**
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check STATIC_ROOT configuration
```

### Debug Commands

```bash
# Check Django configuration
python manage.py check --deploy

# Test database connection
python manage.py dbshell

# View current settings
python manage.py shell -c "from django.conf import settings; print(settings.DEBUG)"
```

## 💰 Railway Pricing

### Free Tier
- **$5 credit** per month
- **512MB RAM** per service
- **Shared CPU**
- **1GB storage**

### Paid Plans
- **$5/month**: 1GB RAM, dedicated CPU
- **$10/month**: 2GB RAM, dedicated CPU
- **Custom**: Enterprise plans available

## 🎯 Next Steps

1. **Monitor your app** in Railway dashboard
2. **Set up custom domain** (optional)
3. **Configure automatic deployments** from GitHub
4. **Set up monitoring alerts**
5. **Scale as needed**

## 📞 Support

- **Railway Docs**: [docs.railway.app](https://docs.railway.app)
- **Community**: [Railway Discord](https://discord.gg/railway)
- **Email**: support@railway.app

---

**Your Django app will be live at: `https://your-app-name.railway.app`** 🎉 