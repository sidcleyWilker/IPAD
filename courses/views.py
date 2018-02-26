from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail

from .models import Course
from .forms import ContactCourse

'''
Página dos cursos
'''
def index_courses(request):
    cursos = Course.object.all()
    template = loader.get_template('courses/index_courses.html')
    context = {
        'cursos' : cursos
    }
    return HttpResponse(template.render(context, request))


def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    template = loader.get_template('courses/details.html')

    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_email(course)
            form = ContactCourse()
    else:
        form = ContactCourse()

    context['form'] = form
    context['course'] = course

    return HttpResponse(template.render(context, request))