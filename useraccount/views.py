from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.views import View
from useraccount.models import UserAccount
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/login.html')
    
    def post(self, request, *args, **kwargs):
        studentId = request.POST.get('studentId')
        password = request.POST.get('password')
        user = authenticate(studentId = studentId, password = password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Student Id or Password')
            return redirect('login')
    


class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/signup.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('user')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('emailaddress')
        studentId = request.POST.get('studentId')
        dept = request.POST.get('dept')
        password = request.POST.get('pass1')


        user_data = {
            'first_name':first_name,
            'last_name':last_name,
            'username':username,
            'email':email,
            'studentId':studentId,
            'dept':dept,
        }


        if UserAccount.objects.filter(username=username):
                messages.info(request, 'Username already exist')
                return render(request, 'user/signup.html',user_data)
        if UserAccount.objects.filter(email=email):
                messages.info(request, 'Email already exist')
                return render(request, 'user/signup.html',user_data)
        if UserAccount.objects.filter(studentId=studentId):
                messages.info(request, 'Student ID already exist')
                return render(request, 'user/signup.html',user_data)
        if len(username) > 20 or len(username) < 4:
                messages.success(request, 'Username length must will be 6-20 Charecter')
                return render(request, 'user/signup.html',user_data)
        try:
            user = UserAccount.objects.create_user(username=username,first_name = first_name,last_name = last_name,email = email, studentId = studentId,password=password, dept= dept)
            user.set_password(password) 
            user.save()
            messages.success(request, 'Successfully Create an account!')
            return render(request, 'user/login.html')
        except:
            messages.success(request, 'Please Fill all required Field.')
            return render(request, 'user/signup.html',user_data)
    





class LogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return redirect('home')