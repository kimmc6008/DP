from django.shortcuts import render, redirect
from .models import TodoList
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.contrib import messages

from .forms import list, CreateUserForm

# Create your views here.
# def home(request):
#     return render(request, 'base.html')


@login_required(login_url='login')
def new_search(request):
    search = request.POST.get('search')
    print(search)
    frontend = {
        'search': search,
    }
    return render(request, 'search.html', frontend)


@login_required(login_url='login')

def home(request):
    todos = TodoList.objects.filter(user=request.user)

    return render(request, 'base.html', {'todos': todos})


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin', 'users'])
def createMarkEight(request):
    form = list()
    if request.method == 'POST':
        form = list(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'create_list.html', context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin', 'users'])
def updateMarkEight(request, pk):
    mark = TodoList.objects.get(id=pk)
    form = list(instance=mark)

    if request.method == 'POST':
        form = list(request.POST, instance=mark)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'create_list.html', context)


@login_required(login_url='login')
# @allowed_users(allowed_roles=['admin', 'users'])
def deleteMarkEight(request, pk):
    mark = TodoList.objects.get(id=pk)

    if request.method == 'POST':
        mark.delete()
        return redirect('home')

    context = {'mark': mark}
    return render(request, 'delete_list.html', context)


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='users')
            user.groups.add(group)

            messages.success(request, "Welcome to Jayden's website, " + username + "!!")

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username OR Password is incorrect :(')

    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')