from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from account .models import *
from .models import *
from .forms import *

def stu_dashboard(request):
        coursest =Courses.objects.all()
        return render(request,'student/home.html',{'coursest':coursest})

def tea_dashboard(request):
        questions= Question.objects.filter(is_taken=False)
        return render(request,'student/teacher.html',{'questions':questions})

def Questionf(request):
        if request.method == 'POST':
                form = QuestionForm(request.POST)
                if form.is_valid():
                        new_question=form.save(commit=False)
                        new_question.asked_by = request.user
                        new_question.save()
                        return HttpResponse('You have succesfully askesd a question')
        else:
                form = QuestionForm()
        return render(request,'student/question.html', {'form': form})
