from django.urls import path

from . import views

urlpatterns = [
     path('', views.RandomWord.as_view(), name='index'),
     path('search/<str:query>', views.SearchWord.as_view(), name='search'),
     path('get/<str:query>', views.GetWord.as_view(), name='get'),
]