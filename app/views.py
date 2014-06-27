from django.http import HttpResponse
from django.shortcuts import render
# from django.conf import settings
from .tasks import send_mail

def home(request):
  if request.method == "POST":
    
    target_email = request.POST.get('target-email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    #because of demo purpose, I don't want validate data but you should do it on real site.
    res_queue = send_mail.delay( target_email, subject, message )

    #Indicate email is sent
    args = {
      'status':'sent'
    }
    return render(request, 'index.html',args)
  else:

    return render(request, 'index.html')

