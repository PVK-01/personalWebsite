from django.shortcuts import render
from django.http import HttpResponse
import templates


def AboutMe(request):
    return render(request, 'AboutMe.html')


def WorkExperience(request):
    return render(request, 'WorkExperience.html')


def Education(request):
    return render(request, 'Education.html')


def Skills(request):
    return render(request, 'Skills.html')


def DataScience(request):
    return render(request, 'DataScience.html')


def PetroleumEngineering(request):
    return render(request, 'PetroleumEngineering.html')
