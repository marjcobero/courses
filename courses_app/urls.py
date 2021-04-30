from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('courses_app/create', views.create),
    path('courses_app/destroy/<int:course_id>', views.destroy),
    path('courses_app/delete/<int:course_id>', views.delete),
]