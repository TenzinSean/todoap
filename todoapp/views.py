from django.shortcuts import render
from django.views.generic import TemplateView
from .models import TodoItme


# Create your views here.
class HomePageView(TemplateView):
    all_todo_items = TodoItme.objects.all()
    template_name = "home.html"
