from django.urls import path
from . import views as views_cv

urlpatterns = [
    path('cv/', views_cv.cv, name='cv'),
    path('addWE/', views_cv.addWorkExperience, name='addWorkExperience'),

]