from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
from django.urls import reverse
from django.http import Http404
from django.views import generic


def index(request):
    student_list = Student.objects.order_by("-first_name")[:20]

    if request.method == 'POST':
        query = request.POST["query"]
        query_type = request.POST["query_type"]
        if query_type == 'first_name':
            student_list = Student.objects.filter(first_name__startswith=query)[:20]
        if query_type == 'last_name':
            student_list = Student.objects.filter(last_name__startswith=query)[:20]
        if query_type == 'university_id':
            student_list = Student.objects.filter(university_id__startswith=query)[:20]
        # create a form instance and populate it with data from the request:
        

    
    context = {'student_list': student_list}
    return render(request, 'studentapp/index.html', context)

# Create your views here.

def add_to_db(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        university_id = request.POST['university_id']
        email = request.POST['email']
        address = request.POST['address']
        gpa = request.POST['gpa']

        q = Student(university_id=university_id, first_name=first_name, last_name=last_name, email=email, address=address, gpa=gpa)
        q.save()
    
    student_list = Student.objects.order_by("-first_name")[:20]
    context = {'student_list': student_list}
    return render(request, 'studentapp/index.html', context)


class ResultsView(generic.DetailView):
    model = Student
    template_name = 'studentapp/results.html'