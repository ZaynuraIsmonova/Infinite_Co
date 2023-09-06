import requests
from django.conf import settings
from django.shortcuts import render, redirect
from .models import *
from .forms import MessageForm
from django.http import HttpResponse


# Create your views here.


def homeView(request):
    main_details = HomeModel.objects.all()
    services = ServicesModel.objects.all()
    abilities = AbilitiesModel.objects.all()
    portfolios = PortfoliosModel.objects.all()
    partners = PartnersModel.objects.all()
    return render(request, 'home.html', {
        'main_details':main_details, 
        'services':services, 
        'abilities':abilities,
        'portfolios':portfolios,
        'partners':partners
    })
def createView(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            message = f"""
            name: {form.cleaned_data['name']}\nemail: {form.cleaned_data['email']}\nsubject: {form.cleaned_data['subject']}\nmessage: {form.cleaned_data['message']}
            """
            requests.post(f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={settings.CHAT_ID}&text={message} ")
            return HttpResponse("Xabar jo'natildi")
        else:
            return HttpResponse(str(form.errors))
    return redirect('home')
    



#details 

