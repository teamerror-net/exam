from django.shortcuts import render,redirect
from contact.models import Contact,NewsLetter
from django.views import View
# Create your views here.
class ContactView(View):
    def post(self, request, *args, **kwargs):
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        queary = Contact.objects.create(fullname=fullname, email=email, message=message)
        queary.save()
        return render(request, 'user/home.html/')
    
class NewsletterView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        newsletter = NewsLetter.objects.create(email=email)
        newsletter.save()
        return redirect('home')
