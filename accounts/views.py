from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages


# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()
            # return redirect('registerUser')
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(firstName=firstName,lastName=lastName,username=username,email=email,password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request,'Your Account has been registred successfully')
            return redirect('registerUser')
        else:
            print('invalid')
            print(form.errors)    
    else:    
        form = UserForm() 
    context = {
        'form' : form, 
    }
    return render(request, 'accounts/registerUser.html', context)