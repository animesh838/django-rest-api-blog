#!/usr/bin/env python
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
sys.path.append('/app')

# Initialize Django
django.setup()

# Import and run migrations
from django.core.management import execute_from_command_line

print("Running Django migrations...")
execute_from_command_line(['manage.py', 'migrate'])
print("Migrations completed!") 