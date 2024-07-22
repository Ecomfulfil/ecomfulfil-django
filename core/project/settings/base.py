from typing import List

DEBUG = False
SECRET_KEY = NotImplemented

ALLOWED_HOSTS: List[str] = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS: List[str] = []

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "django_filters",
    "debug_toolbar",
    "storages",
    # Apps
    "core.accounts.apps.AccountsConfig",
    "core.blocks.apps.BlocksConfig",
    "core.comments.apps.CommentsConfig",
    "core.config.apps.SettingsConfig",
    "core.recipes.apps.RecipesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "core.project.asgi.application"
WSGI_APPLICATION = "core.project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ecomfulfil_backend",
        "USER": "postgres",
        "PASSWORD": "ecomfulfil_backend",
        "HOST": "db",
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
        # TODO(dmu) MEDIUM: Unfortunately Daphne / ASGI / Django Channels do not properly reuse database connections
        #                   and therefore we are getting resource (connection) leak that leads to the following:
        #                   django.db.utils.OperationalError: FATAL:  sorry, too many clients already
        #                   `'CONN_MAX_AGE': 0` is used as workaround. In case it notably affects performance
        #                   implement a solution that either closes database connections on WebSocket client
        #                   disconnect and implement connection pooling outside Django (BgBouncer or similar)
        "CONN_MAX_AGE": 0,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "accounts.Account"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"  # type: ignore # noqa: F821

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # type: ignore # noqa: F821

DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
