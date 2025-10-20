from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# Secret & Debug
# -------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key")
DEBUG = os.getenv("DEBUG") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",") if os.getenv("ALLOWED_HOSTS") else []

# -------------------------------
# Installed Apps
# -------------------------------
INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",
    "rest_framework.authtoken",

    "cloudinary",
    "cloudinary_storage",

    # Your apps
    "mainapp",
]

# -------------------------------
# Middleware
# -------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -------------------------------
# Root URLs and WSGI
# -------------------------------
ROOT_URLCONF = "portfolio_backend.urls"
WSGI_APPLICATION = "portfolio_backend.wsgi.application"

# -------------------------------
# Templates
# -------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # add template dirs if needed
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -------------------------------
# Database (Postgres on Render)
# -------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default=f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
}

# -------------------------------
# Password validation
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------------
# Internationalization
# -------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -------------------------------
# Static files
# -------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# -------------------------------
# Media files (Cloudinary)
# -------------------------------
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
MEDIA_URL = "/media/"

# -------------------------------
# CORS & CSRF
# -------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # local Vite dev
    "https://portfolio-frontend-liard-one.vercel.app",
    "https://portfolio-frontend-git-main-swagaths-projects.vercel.app",
    "https://portfolio-frontend-pl1ixxmdx-swagaths-projects.vercel.app",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    "https://portfolio-frontend-liard-one.vercel.app",
    "https://portfolio-frontend-git-main-swagaths-projects.vercel.app",
    "https://portfolio-frontend-pl1ixxmdx-swagaths-projects.vercel.app",
]

# -------------------------------
# REST Framework
# -------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# -------------------------------
# Cloudinary
# -------------------------------
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}

# -------------------------------
# Default primary key
# -------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
