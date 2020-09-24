from django.urls import path

from . import views

app_name = 'studentapp'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_to_db/', views.add_to_db, name='add_to_db'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results')
    ]
