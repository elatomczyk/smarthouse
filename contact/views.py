#-*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Uzupełnij temat wiadomości!')
        if not request.POST.get('message', ''):
            errors.append('Uzupełnij treść wiadomości!')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Wprowadź poprawny adres e-mail!')
        if not errors:
          try:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'smarthousekrakow@gmail.com'),
                ['smarthousekrakow@gmail.com'],
            )
            return HttpResponse('Thank you, form has been submitted successfully')
          except Exception, err: 
            return HttpResponse(str(err))
    return render(request, 'contact_form.html',
        {'errors': errors})