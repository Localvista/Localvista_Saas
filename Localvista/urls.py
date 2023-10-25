from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from.views import create_html_view
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('business/', include('Business.urls')),
    path('account/', include('Account_App.urls')),

    path('login/', create_html_view('login.html'), name='login'),
    path('logout/', create_html_view('logout.html'), name='logout'),
    path('profile/', create_html_view('profile.html'), name='profile'),
    path('feed/', create_html_view('feed.html'), name='feed'),
    path('settings/', create_html_view('settings.html'), name='settings'),
    path('', create_html_view('landing.html'), name='landing'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
