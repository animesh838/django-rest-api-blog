#!/usr/bin/env python
"""
Simple script to run Django migrations on Railway.
This can be executed in Railway's terminal.
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append('/app')

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Setup Django
django.setup()

# Import Django management commands
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    print("Running Django migrations on Railway...")
    
    # Run migrations
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Create a superuser if needed (optional)
    # execute_from_command_line(['manage.py', 'createsuperuser', '--noinput'])
    
    print("Migrations completed successfully!") 