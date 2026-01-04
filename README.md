# Mini Blog (Django)

A simple Django blog application that displays posts with images, allows visitors to leave comments, and supports "likes" per post (tracked by client IP).

## Features
- List of posts with title, description, author, date, and image
- Post detail page with image, description, author
- Comments form and comments list per post
- Like/Unlike actions (likes tracked by IP address)
- Static assets and media files configured for development

## Tech Stack
- Python
- Django (5.2.x)
- SQLite (default)
- Pillow (for ImageField uploads)

## Project Structure
- `myblog/manage.py` — project entry point
- `myblog/myblog/` — project settings and URLs
- `myblog/blog/` — app with models, views, URLs, migrations
- `templates/blog/` — HTML templates
- `static/css/` — stylesheets
- `media/` — uploaded images

## Prerequisites
- Python 3.11+ recommended
- pip

## Setup
1. Create and activate a virtual environment:
   - macOS/Linux:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows:
     ```
     python -m venv .venv
     .venv\Scripts\activate
     ```

2. Install dependencies:
   ```
   pip install Django Pillow
   ```

3. Apply migrations:
   ```
   python3 myblog/manage.py migrate
   ```

4. (Optional) Create a superuser to access the admin:
   ```
   python3 myblog/manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python3 myblog/manage.py runserver
   ```
   Visit http://127.0.0.1:8000/

## Routes
- `/` — posts list
- `/<id>/` — post detail
- `/review/<id>/` — add comment (POST)
- `/<id>/add_likes/` — add like
- `/<id>/del_likes/` — remove like
- `/admin/` — Django admin

## Models (overview)
- `BlogPost`: title, description, author, date, img
- `Comments`: name, email, text_comments, post (FK)
- `Likes`: ip, post (FK)

## Static & Media
- Static files: served from `static/` in development
- Media files: stored under `media/`, URL at `/media/`
  - Image uploads path: `image/%Y` (by year)

## Notes
- Likes are tracked per IP and do not require authentication.
- This project is configured for development (`DEBUG=True`). Do not use the dev server in production.

