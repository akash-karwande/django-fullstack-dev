# Firstproject (Django 6) – Chai Catalog Demo

A minimal Django 6 project showcasing:
- A simple website with home/about/contact pages
- A feature app named "chai" that lists chai varieties from the database
- Image uploads via ImageField to MEDIA storage
- Static files served from a project-level static directory

This project is intended for learning Django fundamentals: apps, URLs, views, templates, static/media configuration, models, and admin.

## Tech Stack

- Python 3.11+ (recommended)
- Django 6.x
- SQLite (default dev database)
- Pillow (required for ImageField)

## Project Structure

Key files and directories:

```
firstproject/
├─ manage.py
├─ db.sqlite3
├─ firstproject/                 # Project settings and root URLs
│  ├─ settings.py                # TEMPLATES, STATIC, MEDIA configured
│  ├─ urls.py                    # Root URL config and chai include
│  ├─ views.py                   # Home/About/Contact views
├─ chai/                         # Feature app
│  ├─ admin.py                   # Admin registration for ChaiVarities
│  ├─ models.py                  # ChaiVarities model (with ImageField)
│  ├─ urls.py                    # /chai routes
│  ├─ views.py                   # all_chai, order_chai views
│  └─ templates/chai/index.html  # List page for chai varieties
├─ templates/
│  ├─ layout.html
│  └─ website/index.html         # Home page
├─ static/
│  └─ style.css
└─ media/
   └─ chais/                     # Uploaded images land here (ImageField upload_to)
```

## URLs

- / -> Renders templates/website/index.html
- /about/ -> Simple HttpResponse
- /contact/ -> Simple HttpResponse
- /chai -> Lists all chai varieties (renders chai/templates/chai/index.html)
- /chai/order/ -> Placeholder route (see Notes/TODO below)

Note: In root URLConf, `path('chai', include('chai.urls'), ...)` maps "/chai" (no trailing slash) to the chai app. You can optionally switch to `'chai/'` for conventional trailing slash URLs.

## Quick Start

1) Clone or open this folder in your editor/terminal, then create a virtual environment:
```
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

2) Install dependencies:
```
pip install "Django>=6,<7" Pillow
```

3) Apply migrations:
```
python manage.py migrate
```

4) (Optional) Create a superuser for admin access:
```
python manage.py createsuperuser
```

5) Run the development server:
```
python manage.py runserver
```

6) Visit:
- http://127.0.0.1:8000/         (home)
- http://127.0.0.1:8000/chai     (chai list)
- http://127.0.0.1:8000/admin/   (admin)

## Admin and Sample Data

- Admin is enabled (`admin.site.register(ChaiVarities)`).
- Add records for ChaiVarities from the admin (name, description, type, and image).
- The ImageField saves uploads to `media/chais/` (configured by `upload_to='chais/'`).
- Ensure Pillow is installed; otherwise, image uploads will fail.

## Settings Overview

Key configuration in firstproject/settings.py:
- TEMPLATES: `DIRS = ['templates']` (project-level templates directory)
- Static files:
  - `STATIC_URL = 'static/'`
  - `STATICFILES_DIRS = [BASE_DIR / 'static']`
- Media files:
  - `MEDIA_URL = '/media/'`
  - `MEDIA_ROOT = BASE_DIR / 'media'`
- Database: SQLite at `BASE_DIR / 'db.sqlite3'` for development

## chai App Summary

Model (ChaiVarities):
- name: CharField
- image: ImageField(upload_to='chais/')
- description: TextField
- date_added: DateTimeField(default=timezone.now)
- type: CharField with choices (MASALA, GINGER, PLAIN, LEMON)

Views:
- all_chai: queries all ChaiVarities and renders `chai/index.html`
- order_chai: placeholder (see TODO)

Templates:
- Project base templates at `templates/`
- Chai app templates at `chai/templates/chai/`

## Notes and TODO

- The `order_chai` view currently returns a plain string, which is not a valid Django response. Replace with an HttpResponse or render a template, e.g.:
  ```python
  from django.http import HttpResponse

  def order_chai(request):
      return HttpResponse("Order chai page")
  # or
  # return render(request, 'chai/order.html')
  ```
- In `chai/models.py`, ensure `__str__` is indented inside the ChaiVarities model class so the admin displays readable names:
  ```python
  class ChaiVarities(models.Model):
      ...
      def __str__(self):
          return self.name
  ```
- For cleaner URLs, consider changing in root urls.py:
  ```python
  path('chai/', include('chai.urls'))
  ```
- Do not expose `SECRET_KEY` publicly; this project is for local development/learning only.

## Common Commands

```
# Start dev server
python manage.py runserver

# Make and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Load Django shell
python manage.py shell
```

## License

Educational/demo purposes.
