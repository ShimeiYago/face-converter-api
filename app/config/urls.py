# from django.contrib import admin
from django.urls import path, include, re_path
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from rest_framework import permissions
from django.conf import settings
# from django.conf.urls.static import static
# import os

# api_info = openapi.Info(
#     title='API Docs',
#     default_version=f'v{settings.API_VERSION}',
# );

# schema_view = get_schema_view(
#     api_info,
#     public=True,
#     permission_classes=[permissions.AllowAny] if settings.DEBUG else [permissions.IsAdminUser]
# )

urlpatterns = [
    # path(f'{settings.ADMIN_PATH}/', admin.site.urls),
    # path('', include('auths.urls')),
    # path('', include('articles.urls')),
    # path('', include('users.urls')),
    path('', include('convert.urls')),
]

# static files
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     # swagger
#     urlpatterns.append(re_path('docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'))

    # media
    # media_root = os.path.join(settings.BASE_DIR, settings.UPLOAD_DIR)
    # urlpatterns += static(f'{settings.UPLOAD_DIR}/', document_root=media_root)
