
from django.contrib import admin
from django.urls import path
from resume.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addResume/', addResume, name='addResume'),
    path('viewResume/<str:id>', viewResume, name='viewResume'),
    path('editResume/<str:id>', editResume, name='editResume'),
    path('deleteResume/<str:id>', deleteResume, name='deleteResume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
