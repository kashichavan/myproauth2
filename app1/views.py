from django.shortcuts import render,redirect,HttpResponse

from .forms import RegisterForm,User,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method=="POST":
        user=User.objects.filter(username=request.POST.get('username'))
        if user.exists():
            messages.info(request,"User Already Exist")
            return redirect('/register/')
        else:
            form=RegisterForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/login/')
    form=RegisterForm()
    return render(request,'register.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            print("ehllo")
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect('/home/')
            else:
                messages.info(request,"username or password is invalid")
                return redirect('/login/')
    form=LoginForm()
    return render(request,'login.html',{'form':form})
def home(request):
    return HttpResponse("<h1>This is Home page</h1>")

def logout_view(request):
    logout(request)
    return redirect('/login/')


        

    
        
