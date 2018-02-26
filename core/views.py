from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

'''
Página inicial da aplicação
'''
def home(request):
    template = loader.get_template('core/home.html')
    context = {}
    return HttpResponse(template.render(context, request))


'''
Página de contato da aplicação
'''
def contact(request):
    template = loader.get_template('core/contact.html')
    context = {}
    return HttpResponse(template.render(context, request))