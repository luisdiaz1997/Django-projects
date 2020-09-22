from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.urls import reverse
from django.http import Http404
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'studentapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    

# Create your views here.

class DetailView(generic.DetailView):
    model = Question
    template_name = 'studentapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'studentapp/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'studentapp/detail.html', {'question': question, 'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('studentapp:results', args=(question.id,)))
