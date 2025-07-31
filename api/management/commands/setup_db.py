from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Set up database tables and initial data'

    def handle(self, *args, **options):
        self.stdout.write('Setting up database...')
        
        try:
            # Run migrations
            self.stdout.write('Running migrations...')
            call_command('migrate', verbosity=0)
            self.stdout.write(self.style.SUCCESS('Migrations completed successfully!'))
            
            # Check if tables exist
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                table_names = [table[0] for table in tables]
                
            self.stdout.write(f'Database tables: {table_names}')
            
            # Create a test post if none exist
            from api.models import Post
            if Post.objects.count() == 0:
                self.stdout.write('Creating a test post...')
                Post.objects.create(
                    title='Welcome to Django API Blog',
                    content='This is a test post created during setup.',
                    is_published=True
                )
                self.stdout.write(self.style.SUCCESS('Test post created!'))
            
            self.stdout.write(self.style.SUCCESS('Database setup completed successfully!'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error setting up database: {str(e)}'))
            raise 