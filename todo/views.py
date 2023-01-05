from django.shortcuts import render,redirect
from . form import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def task(request):
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            try:
                finish=request.POST('finished')
                if finish == 'on':
                    finish=True
                else:
                    finish=False
            except:
                finish=False
            tasks = Task(
                user=request.user,
                title=request.POST['title'],
                finished=finish
            )
            tasks.save()
        messages.success(request,f'Task added from {request.user.username}')
    else:      
        form=TaskForm()

    task=Task.objects.filter(user=request.user)
    if len(task) == 0:
        tasks_done = True
    else:
        tasks_done = False
    context={
        'form':form,
        'tasks':task,
        'tasks_done':tasks_done

    }
    return render(request,'todo.html',context)

@login_required
def update_task(request,pk=None):
    task= Task.objects.get(id=pk)
    if task.finished == True:
        task.finished = False
    else:
        task.finished = True

    task.save()
    return redirect('todo')

@login_required
def delete_task(request,pk=None):
    Task.objects.get(id=pk).delete()
    return redirect('todo')


def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Create for {username} !')
            #return redirect('login')

    else:
        form=RegistrationForm()
    context={
        'form':form
    }
    return render(request,'register.html',context)