from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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