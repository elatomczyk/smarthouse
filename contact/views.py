#-*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Uzupełnij temat wiadomości!')
        if not request.POST.get('message', ''):
            errors.append('Uzupełnij treść wiadomości!')
        if request.POST.get('email2') and '@' not in request.POST['email2']:
            errors.append('Wprowadź poprawny adres e-mail!')
        if not errors:
            try:
                message = "Email: "+request.POST['email2']+" \n Wiadomosc: "+request.POST['message']
                message.encode('utf-8')
                send_mail(
                    request.POST['subject'],
                    message,
                    request.POST['email2'],
                    ['et17@onet.pl'],
                    fail_silently=False
                )
                # email = EmailMultiAlternatives('Subject', 'Body', to=['et17@onet.pl'])
                # email.send()
                print message

                # send_mail('Subject here', 'Here is the message.', 'from@example.com',['to@example.com'], fail_silently=False)
                print request.POST['email2']
                return HttpResponseRedirect("/")

            except Exception, err:
                return HttpResponse(str(err))
    return render(request, 'contact_form.html',
        {'errors': errors})