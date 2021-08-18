from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = NewUserForm()
    return render(request, 'account/register.html', {"form": form})


@login_required
def account(request):
    return render(request, 'account/account.html')


@login_required
def address(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        zip = request.POST.get('zip')
        phone = request.POST.get('phone')
        User.objects.filter(id=pid).update(first_name=first_name, last_name=last_name, address=address, zip=zip,
                                           phone=phone)
        return redirect("address")
    else:
        pass
    return render(request, 'account/address.html')
