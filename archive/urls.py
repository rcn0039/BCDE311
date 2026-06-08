from django.urls import path

from . import views

app_name = "archive"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path('project/<int:id>/', views.project, name='project'),
]