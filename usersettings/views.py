from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views import View
from useraccount.models import UserAccount
# Create your views here.
class UserSettingsView(View):
    def get(self, request, *args, **kwargs):
        login_user = UserAccount.objects.get(id=request.user.id)
        data = {
            'login_user': login_user
        }
        return render(request, 'user/settings.html',context=data)
    
    def post(self, request, *args, **kwargs):
        login_user = UserAccount.objects.get(id=request.user.id)
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        auth_user = authenticate(studentId = login_user.studentId, password = old_password)
        if new_password == confirm_password:
            try:
                if auth_user is not None:
                    auth_user.set_password(new_password)
                    auth_user.save()
                    messages.success(request, 'Successfully updated password')
                    return redirect('settings')
                else:
                    messages.warning(request, 'Invalid Password')
                    return redirect('settings')
            except:
                pass
        else:
            messages.info(request, 'Password is not match')
            return redirect('settings')