from django.contrib.auth.views import logout
from django.core.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from account.forms import FormRegister

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")

def register_user(request):
    if request.method == 'POST':
        form = FormRegister(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('register_success')
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = FormRegister()
    print args
    return render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')