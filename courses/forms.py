from django import forms
from django.core.mail import send_mail

class ContactCourse(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem / Dúvida',
        widget=forms.Textarea
    )

    def send_email(self, course):
        subject = '[%s] Contato' % course

        send_mail(
            subject,
            self.cleaned_data['message'],
            self.cleaned_data['email'],
            ['sidcleywilker@gmail.com'],
            fail_silently=False,
        )