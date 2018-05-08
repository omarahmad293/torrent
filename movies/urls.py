from django.urls import path
from . import views

urlpatterns = [

    # /movies/
    path('', views.index, name='index'),

    # /movies/{album_id}/
    path('<movie_id>/', views.detail, name='detail'),
]
