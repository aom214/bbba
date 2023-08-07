"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _

admin.site.site_header= "Harry Potter"
admin.site.site_title="Harry Potter"
admin.site.index_title="Harry Potter"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('harryshop.urls')),
    path('jet/',include('jet.urls','jet')),
    path('jet/dashboard/',include('jet.dashboard.urls','jet-dashboard')),
    path('',include('app.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
