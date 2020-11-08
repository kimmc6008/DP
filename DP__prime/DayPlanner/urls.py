from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
    path('list_delete', views.deleteMarkEight, name='delete_list'),
    path('list_add', views.createMarkEight, name='create_list'),
    path('list_update', views.updateMarkEight, name='update_list'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
]