from django.shortcuts import redirect, render
import requests
from .models import *

def Home(request):
    ozim = Ozim.objects.all()
    picture = Picture.objects.all()
    bilim = Bilim.objects.all()
    context = {
        'picture' : picture,
        'ozim' : ozim,
        'bilim':bilim
     }


    return render(request, 'index.html', context)

def SendMsg(request):
     
    name =  request.POST['name']
    email =  request.POST['email']
    message =  request.POST['message']


    
    bot_token = '6763362803:AAHtSbcpdhjnxkudr8R_vFYvN1sIXHUkipI'
    text = 'Saytdan xabar: \n\nIsmi : ' + name + '\nemail : ' + email + '\nxabar : ' + message
    url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='
    requests.get(url + '6516071223' + '&text=' + text)

    return redirect('/')

  