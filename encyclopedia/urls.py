from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>" , views.title_page , name="title_page"),
    path("new_page" , views.new_page , name='new_page') ,
    path("edit_page/<str:title>" , views.edit_page , name='edit_page')
]
