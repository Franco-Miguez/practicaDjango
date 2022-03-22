from django.views.generic import view
from django.shortcuts import render

class HomeView(view):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'index.html', context)