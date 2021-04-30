from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "all_courses": Course.objects.all()
    }
    return render(request, 'course.html', context)

def create(request):
    if request.method == "POST":
        errors = Course.objects.create_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        course = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, course_id):
    context = {
        'a_course': Course.objects.get(id=course_id)
    }
    return render(request, "destroy.html", context)

def delete(request, course_id):
    if request.method == "POST":
        to_delete = Course.objects.get(id=course_id)
        to_delete.delete()
    return redirect('/')