from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import connection
import logging

logger = logging.getLogger(__name__)

def home(request):
    """Home page view"""
    return render(request, 'home.html')

def posts(request):
    """Posts page view"""
    return render(request, 'posts.html')

@login_required
def admin_redirect(request):
    """Redirect to admin panel"""
    from django.shortcuts import redirect
    return redirect('/admin/')

def health_check(request):
    """Health check endpoint to debug database issues"""
    try:
        # Check if database tables exist
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='api_post';")
            tables = cursor.fetchall()
        
        # Check if we can query the Post model
        from api.models import Post
        posts_count = Post.objects.count()
        
        return JsonResponse({
            'status': 'healthy',
            'database_tables_exist': bool(tables),
            'posts_count': posts_count,
            'database_name': connection.settings_dict.get('NAME', 'unknown')
        })
    except Exception as e:
        logger.error(f"Health check error: {str(e)}")
        return JsonResponse({
            'status': 'unhealthy',
            'error': str(e)
        }, status=500) 