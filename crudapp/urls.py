from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('form/',views.insert_info,name='form'),
    path('update/<int:id>', views.update_info,name='update'), 
    path('delete/<int:id>',views.delete_info,name='delete'),
]