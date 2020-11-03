from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<em>Second app</em>')


def help(request):
    help_content = {
        "help_topic": "Help topic 1"
    }
    return render(request, 'secondapp/help.html', context=help_content)
