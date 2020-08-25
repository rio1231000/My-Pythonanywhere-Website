from django.urls import path
from . import views as views_lists

urlpatterns = [
    path('lists/', views_lists.lists, name='lists'),

]