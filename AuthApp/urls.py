from django.contrib import admin
from django.urls import path, include

from asite import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret_page/', views.secret_page, name='secret_page'),
    path('secret/', views.SecretPage.as_view(), name='secret'),
    path('admin/', admin.site.urls),
]
