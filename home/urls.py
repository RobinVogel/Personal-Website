from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('research/', views.research, name='research'),
    path('blog/', views.blog, name='blog'),
    path('blog/<str:url_name>', views.article, name='article')
]
