from django.urls import path
from .views import BlogViewsList, BlogCreateView
app_name = 'blog'

urlpatterns = [
    path('', BlogViewsList.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name='create' )
]
