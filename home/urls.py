from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>', views.task_details, name='details'),
    path('edit/<int:id>', views.edit_task, name='edit'),
    path('delete/<int:id>', views.delete_task, name='delete'),
]
