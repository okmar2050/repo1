from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from testapp.forms import SignupForm


def home_view(requset):
    return render(requset,'testapp/home.html')
def signup_view(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect ('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
@login_required
def java_exam(request):
    return render(request,'testapp/javaexam.html')
def python_exam(request):
    return render(request,'testapp/pythonexam.html')
def apptitude_exam(request):
    return render(request,'testapp/apptitudeexam.html')
