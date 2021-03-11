from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:subject_id>/', views.detail, name='detail'),
    path('<int:subject_id>/answers', views.answers, name='answers'),
    path('<int:subject_id>/vote', views.vote, name='vote')
]