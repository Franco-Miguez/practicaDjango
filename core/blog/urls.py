from django.urls import path
from .views import BlogViewsList
app_name = 'blog'

urlpatterns = [
    path('', BlogViewsList.as_view(), name="home")
]
