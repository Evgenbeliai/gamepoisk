from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import *
def regist(request):

    if request.method=='POST':
        form = CustomUserCreationform(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Norm')
            print('aaaa')
            return redirect('start')
        else:
            print('bbbbb')
            form = CustomUserCreationform(request.POST, request.FILES)
    else:
        print('ccccc')
        form = CustomUserCreationform()
    return render(request, 'regist.html', {'form':form})
# Create your views here.
