from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import SignupForms,profileForms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,UserChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages


# Create your views here.
def sign_up(request):
    if request.method=='POST':
       fm= SignupForms(request.POST)
       if fm.is_valid():
           fm.save()
    else:
        fm=SignupForms()
    return render(request,'enroll/signup.html',{'form':fm})
def log_in(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm()
    return render(request,'enroll/login.html',{'form':fm})
def profile(request):
    if request.user.is_authenticated:
      fm=profileForms(instance=request.user)
      return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
def change_pass(request):
    if request.method=='POSt':
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
           fm.save()
           update_session_auth_hash(request,fm.user
                                    )
           messages.success(request,'Success Fully updated')
           return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)


        return render(request,'enroll/changepass.html',{'form':fm })
    else:
        return HttpResponseRedirect('/login/')