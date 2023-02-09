from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from .forms import *

def index(request):
    return render(request, 'ilya_rest/index1.html', locals())

def work(request):
    orders = Order.objects.all()
    if request.method == "POST":
        form = OrderForm(request.POST)
        form.save()
        return render(request, 'ilya_rest/index_work.html', context)

    form = OrderForm()
    context = {
        'form': form,
        'orders': orders
    }
    return render(request, 'ilya_rest/index_work.html', context)


#def in_cart(request):
#    return render(request, 'ilya_rest/index_cart.html', locals())

def about(request):
    comments = Comment.objects.all()

    context = {
        'comments': comments
    }
    return render(request, 'ilya_rest/index_about.html', context)

def comment(request):

    if request.method == "POST":
        form = AdderForm(request.POST)
        form.save()
        return redirect('/feedback')

    form = AdderForm()
    context = {
        'form': form
    }
    return render(request, 'ilya_rest/index_leave_c.html', context)

@csrf_exempt
def login_(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    print(username, password)
    if username is None or password is None:
        return render(request, 'ilya_rest/login.html', locals())
    else:
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                error = "Error of user authentication"
                return render(request, 'ilya_rest/login.html', locals())
        else:
            error = "User is incorrect"
            return render(request, 'ilya_rest/login.html', locals())

def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def registration_(request):
    if request.method == "POST":
        print("post")
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        print(username, password)
        if password != password2:
            print("Пароль не подтвержден")
            return HttpResponseRedirect('/')
        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                print("Такой пользователь уже существует")
            else:
                user = User.objects.create_user(username=username, password=password, email=password+'@mail.ru')
                user.save()
        except:
            print("unknown error")
        if username is None or password is None:
            return render(request, 'registration.html',
                          locals())
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
    return render(request, 'ilya_rest/registration.html', locals())
