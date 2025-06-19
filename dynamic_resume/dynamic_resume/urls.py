
from django.contrib import admin
from django.urls import path
from resume.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addResume', addResume, name='addResume'),
    path('viewResume', viewResume, name='viewResume'),
    path('editResume', editResume, name='editResume'),
    path('deleteResume', deleteResume, name='deleteResume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
