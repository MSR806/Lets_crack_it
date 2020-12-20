from django.shortcuts import render, redirect
from main.models import solution
from django.contrib import messages
from django.contrib.auth.models import User,auth



def index(request):
    solutions = solution.objects.all()
    context = {'sols': solutions}
    return render(request, 'index.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/login')
    return render(request, 'Login.html')

def addsolution(request):
    context = {'success': False}
    if request.method == 'POST':
        question_p = request.POST['question']
        solution_p = request.POST['solution']

        print(question_p, solution_p)
        ins = solution(question= question_p, solution= solution_p)
        ins.save()
        context = {'success': True}
    return render(request, 'AddSolution.html', context)

def logout(request):
    auth.logout(request)
    return redirect('/')