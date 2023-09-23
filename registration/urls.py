"""
URL configuration for registration project.

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
from app1 import views
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

# in urlpattern we give different path to web page
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('signup.html',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('login.html',views.LoginPage,name='login'),
    path('UploadBook',views.UploadBook,name='UploadBook'),
    path('login/signup.html',views.SignupPage,name='signup'),
    path('logout/',views.LoginPage,name='logout'),
    path('login/',views.UploadBook,name='logout'),

]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# the above path is given for creating a media file to store all document files