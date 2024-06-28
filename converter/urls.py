from django.urls import path
from . import views

urlpatterns = [
    path('',views.also_known, name ='also_known'),
    path('convert/', views.convert_number_to_words_view, name='convert_number_to_words'),
]

