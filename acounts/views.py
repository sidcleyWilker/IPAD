from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, EditAcountForm, PasswordResetForm
from .models import PasswordReset

def register(request):
    template = loader.get_template('acounts/register.html')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            '''apos o cadastro o usuario já entra direto no site'''
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def password_reset(request):
    template = loader.get_template('acounts/password_reset.html')
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return HttpResponse(template.render(context, request))


def password_reset_confirm(request, key):
    template = loader.get_template('acounts/password_reset_confirm.html')
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return HttpResponse(template.render(context, request))


@login_required()
def dashboard(request):
    template = loader.get_template('acounts/dashboard.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

@login_required()
def edit(request):
    template = loader.get_template('acounts/edit.html')
    context = {}
    if request.method == 'POST':
        form = EditAcountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAcountForm(instance=request.user)
            context['success'] = True
            #return redirect('acounts:dashboard')
    else:
        form = EditAcountForm(instance=request.user)
    context['form'] = form

    return HttpResponse(template.render(context, request))


@login_required
def edit_password(request):
    template = 'acounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form

    return render(request, template, context)