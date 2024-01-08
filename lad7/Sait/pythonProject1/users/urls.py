from django.urls import path
from . import views
urlpatterns = [
path('', views.get_name, name='user_name'),
path('user/search', views.user_by_name, name='user_by_name'),
path('user/search_2', views.user_by_name_2, name='user_by_name_2'),
path('user/search_3', views.user_by_name_3, name='user_by_name_3'),

]