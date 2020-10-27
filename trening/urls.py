from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.register, name='trening-create'),
    path('results/', views.results.as_view(), name='trening-results')
]
