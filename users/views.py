from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect


from django.views import View

from users.forms import UserRegisterForm, UserUpdateForm


class RegisterView(View):
    def get(self, request):
        create_form=UserRegisterForm()
        context = {'create_form': create_form}
        return render(request,'users/register.html', context)
    def post(self, request):
        user_form=UserRegisterForm(data=request.POST)
        if user_form.is_valid():
           user_form.save()
           return redirect('login')
        else:
            context = {'create_form':user_form}
            return render(request,'users/register.html',context)


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {'form': form}
        return render(request,'users/login.html', context)

    def post(self, request):
        login_form=AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user=login_form.get_user()
            login(request,user)
            messages.success(request,'You have successfully logged in')
            return redirect('book-list')
        else:
            return render(request,'users/login.html', {"login_form":login_form})
        # user_form=UserLoginForm(data=request.POST)
        # if user_form.is_valid():
        #     data = user_form.cleaned_data
        #     user= authenticate(username=data['username'], password=data['password'])
        #     if user is not None:
        #         if user.is_active:
        #             login(request, user)
        #             return HttpResponse('You are now logged in')
        #         else:
        #             return HttpResponse('Your account is inactive')
        #     else:
        #         return HttpResponse('Invalid login details')




# Create your views here.
class ProfileView(LoginRequiredMixin,View):
    def get(self, request):

        return render(request,'users/profile.html',{'user':request.user})
class LogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        messages.info(request,'You have been logged out')
        return redirect('home')


class ProfileEditView(LoginRequiredMixin,View):
    def get(self, request):
        user_update_form=UserUpdateForm(instance=request.user)
        return render(request,'users/profile_edit.html',{"form":user_update_form})
    def post(self, request):
        user_update_form=UserUpdateForm(data=request.POST,instance=request.user,files=request.FILES)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request,'You have successfully updated your profile')
            return redirect('profile')
        return render(request,'users/profile_edit.html',{"form":user_update_form})
