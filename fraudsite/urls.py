
from django.urls import path
from fraudapp import views
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_csv, name='upload'),
]
