# Django REST Framework Full-Stack Website

A modern full-stack web application built with Django REST Framework for the backend API and a responsive frontend with Tailwind CSS.

## Features

- **REST API**: Complete CRUD operations with Django REST Framework
- **Modern Frontend**: Responsive design with Tailwind CSS and JavaScript
- **Database Models**: Posts and Comments with proper relationships
- **Admin Interface**: Django admin panel for content management
- **Authentication**: User authentication and permissions
- **CORS Support**: Configured for frontend integration

## Project Structure

```
django_project/
├── api/                    # API app with models, views, serializers
├── myproject/             # Main Django project settings
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── media/                 # User uploaded files
├── requirements.txt       # Python dependencies
└── manage.py             # Django management script
```

## Setup Instructions

### 1. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Database Migrations
```bash
python manage.py migrate
```

### 4. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```
**Default admin credentials:**
- Username: `admin`
- Password: `admin123`

### 5. Start Development Server
```bash
python manage.py runserver
```

### 6. Access the Application
- **Frontend**: http://127.0.0.1:8000/
- **Posts Page**: http://127.0.0.1:8000/posts/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **API Root**: http://127.0.0.1:8000/api/

## API Endpoints

### Posts
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create new post
- `GET /api/posts/{id}/` - Get specific post
- `PUT /api/posts/{id}/` - Update post
- `DELETE /api/posts/{id}/` - Delete post
- `GET /api/posts/published/` - Get published posts only
- `POST /api/posts/{id}/add_comment/` - Add comment to post

### Comments
- `GET /api/comments/` - List all comments
- `POST /api/comments/` - Create new comment
- `GET /api/comments/{id}/` - Get specific comment
- `PUT /api/comments/{id}/` - Update comment
- `DELETE /api/comments/{id}/` - Delete comment

### Users
- `GET /api/users/` - List all users (authenticated only)
- `GET /api/users/{id}/` - Get specific user (authenticated only)

## Frontend Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Interactive UI**: Create, read, update, delete posts
- **Modern Styling**: Tailwind CSS with smooth animations
- **Real-time Updates**: JavaScript-powered dynamic content
- **Modal Dialogs**: For creating and editing content
- **Error Handling**: User-friendly error messages

## Database Models

### Post Model
- `title`: CharField (max 200 characters)
- `content`: TextField
- `author`: ForeignKey to User
- `created_at`: DateTimeField (auto-created)
- `updated_at`: DateTimeField (auto-updated)
- `is_published`: BooleanField (default False)

### Comment Model
- `post`: ForeignKey to Post
- `author_name`: CharField (max 100 characters)
- `content`: TextField
- `created_at`: DateTimeField (auto-created)

## Development

### Adding New Features
1. Create models in `api/models.py`
2. Create serializers in `api/serializers.py`
3. Create views in `api/views.py`
4. Add URL patterns in `api/urls.py`
5. Create migrations: `python manage.py makemigrations`
6. Apply migrations: `python manage.py migrate`

### Frontend Development
- Templates are in `templates/` directory
- Static files in `static/` directory
- Uses Tailwind CSS for styling
- JavaScript for interactive features

### API Development
- Uses Django REST Framework ViewSets
- Automatic serialization/deserialization
- Built-in authentication and permissions
- Pagination support
- CORS configured for frontend integration

## Production Deployment

### Environment Variables
Create a `.env` file in the project root:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
```

### Static Files
```bash
python manage.py collectstatic
```

### Database
Consider using PostgreSQL for production:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Technologies Used

- **Backend**: Django 5.2.4, Django REST Framework 3.15.2
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: HTML5, CSS3 (Tailwind CSS), JavaScript (ES6+)
- **HTTP Client**: Axios for API requests
- **Authentication**: Django's built-in authentication system
- **CORS**: django-cors-headers for cross-origin requests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License. 