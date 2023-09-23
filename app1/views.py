from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import UploadBookForm


@login_required(login_url='') #this decorater is used to restrict bypassing to other pages
def UploadBook(request):
    if request.method == 'POST':  #post 
        form = UploadBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = UploadBookForm()
        context = {
            'form':form,
        }
    return render(request, 'UploadBook.html', context)
#   writing function for signup page and login page to  
def SignupPage(request):
    if request.method=='POST':
        ufname=request.POST.get('firstname')
        usname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password!=cpassword:
            return HttpResponse("your passward doest match!!!!")
        else:    
            my_user=User.objects.create_user(ufname,email,password)
            my_user.save
            # return HttpResponse("user created succesfully")
            return redirect('login')
            # print(ufname,usname,email,password,cpassword)

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        passw=request.POST.get('passw')
        # we are using autehntiacate function from django to autehnticate the username and passward
        user=authenticate(request,username=username,password=passw)
        # we are making a constraint if details are correct than user can login otherwise error message is thrown
        if user is not None:
            login(request,user)
            return redirect('UploadBook')
        else:
            return HttpResponse("incorrect username and passward")

                          
        # print(username,passw) to ckeck the working of function


    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
        
# writen by ayush