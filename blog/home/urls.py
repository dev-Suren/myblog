from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('blog-detail/<slug>', blog_detail, name="blog_detail"),
    path('login/', login_logic, name='login_logic'),
    path('profile/', admin_page, name='admin_page'),
]
