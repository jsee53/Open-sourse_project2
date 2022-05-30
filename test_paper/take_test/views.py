from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Exam
import json

# Create your views here.
def take_test(request):
    return render(request, "take_test/index.html")