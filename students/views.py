from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [{'id': 1, 'name': 'John', 'age': 20}, {'id': 2, 'name': 'Jane', 'age': 22}]
    return HttpResponse(students)