"""
URL configuration for deployment_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views as token_views

# URL routing for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('api/', include('api.urls')),  # Include the URLs from the 'api' app
    path('api-auth/', include('rest_framework.urls')),  # For browsable API login
    path('api-token-auth/', token_views.obtain_auth_token),  # Token authentication endpoint
]