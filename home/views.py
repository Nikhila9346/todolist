from django.shortcuts import render, redirect
from .models import ToDoList


# Create your views here.

def home(request):
    details = ToDoList.objects.all().order_by('-id')
    #create operation
    if request.method == 'POST':
        tname = request.POST['tname']
        tdesc = request.POST['tdesc']

        ToDoList.objects.create(
            name=tname,
            desc=tdesc
        )
        return redirect('home')

    context = {
        'data': details,
    }

    return render(request, 'home.html', context)

def edit_task(request, id):
    data = ToDoList.objects.get(id=id)

    # print(request.POST)
    # print(request.POST['tname'])
    # print(request.POST['tdesc'])
    if request.method == 'POST':
        # print(request.POST)
        tname = request.POST['tname']
        tdesc = request.POST['tdesc']
        # print(tname)
        # print(tdesc)

        data.name = tname 
        data.desc = tdesc

        data.save()
        # print(data.name)
        # print(data.desc)

        return redirect('home')

    context={
        'data':data,
    }
    return render(request, 'form.html', context)

def delete_task(request, id):
    data = ToDoList.objects.get(id=id)

    data.delete()
        # print(request.POST)

    return redirect('home')
    


def task_details(request, id):
    task = ToDoList.objects.get(id=id)

    context = {
        'data':task
    }
    return render(request, 'details.html', context)