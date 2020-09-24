from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from django.urls import reverse
from django.http import Http404
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'studentapp/index.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.order_by("-first_name")[:5]
    

# Create your views here.

class DetailView(generic.DetailView):
    model = Student
    template_name = 'studentapp/detail.html'


class ResultsView(generic.DetailView):
    model = Student
    template_name = 'studentapp/results.html'