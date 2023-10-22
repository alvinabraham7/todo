from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .models import Task
from . forms import form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class TaskListview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'

class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = ('list')


class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = 'name','priority','date'




    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})
def index(request):
    res = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date', '')
        task = Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"index.html",{'result':res})

# def detail(request):
#
#     return render(request,"detail.html",)

def delete(request,taskid):
    if request.method == 'POST':
        taskout = Task.objects.get(id=taskid)
        taskout.delete()
        return redirect('/')
    return render(request,"delete.html")


def update(request,id):
    task = Task.objects.get(id=id)
    f = form(request.POST or None,instance=task)

    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{'f':f,'task':task})

