from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as loginViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("blog.urls")),
    path('registration/', userViews.register, name='registration'),
    path('profile/', userViews.profile, name='profile'),
    path('login/', loginViews.LoginView.as_view(template_name='users/user.html'), name='login'),
    path('exit/', loginViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
