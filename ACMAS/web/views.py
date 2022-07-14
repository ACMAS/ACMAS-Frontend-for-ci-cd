from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt


# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def searchByQuestion(request):
    return render(request, 'search-by-question.html')


def searchByCourse(request):
    return render(request, 'search-by-course.html')


def uploadSearch(request):
    return render(request, 'upload-search.html')


def getQuestionInput(request):
    question = request.GET.get('question')
    if len(question) == 0:
        print("No question input")
    else:
        print(question)
