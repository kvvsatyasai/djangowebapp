from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# @login_required(login_url='signin')
def editing(request):
    return render(request, "myapp/Editing.html", {})

def  editor(request):
    return render(request, "myapp/Editor.html", {})

def welcome(request):
    return render(request, "myapp/welcome.html", {})



def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse('<p style="font-size: 35px; font-weight: bold;">Your password and confrom password are not Same!!</p>')
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('signin')


    return render(request,"myapp/signup.html", {})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('Editor')
        else:
            return HttpResponse('<p style="font-size: 35px; font-weight: bold;">Username or Password is incorrect!!!</p>')
    return render(request,"myapp/signin.html", {})

def LogoutPage(request):
    logout(request)
    return redirect('signin')
# Create your views here.
