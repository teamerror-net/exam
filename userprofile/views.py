from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from useraccount.models import UserAccount
# Create your views here.
class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        login_user = UserAccount.objects.get(id=request.user.id)
        data = {
            'login_user': login_user
        }
        return render(request, 'user/profile.html',context=data)

    def post(self, request, *args, **kwargs):
        login_user = UserAccount.objects.get(id=request.user.id)
        profile_pic = request.FILES['profile_pic']
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        login_user.profile_pic = profile_pic
        login_user.first_name = first_name
        login_user.last_name = last_name
        login_user.email = email
        login_user.phone = phone
        login_user.save()
        messages.success(request, 'Successfully update profile')
        return redirect('profile')
