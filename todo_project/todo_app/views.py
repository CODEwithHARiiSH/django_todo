from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todo_forms
from .models import todo
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class todolistview(ListView):
    model = todo
    template_name = 'home.html'
    context_object_name = "temp"

class todoDetailview(DetailView):
    model = todo
    template_name = 'detail.html'
    context_object_name = "task"




class todoUpdateview(UpdateView):
    model = todo
    template_name = 'edit.html'
    context_object_name = "task"
    fields=('task', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs= {'pk':self.object.id})

class todoDeleteview(DeleteView):
    model = todo
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')




def home(request):
    tasks=todo.objects.all()

    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=todo(task=name,priority=priority,date=date)
        task.save()

    return render(request, 'home.html',{'temp':tasks})


def delete(request,taskid):
    task = todo.objects.get(id=taskid)
    if request.method=='POST':

        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request, id):
    idd = todo.objects.get(id=id)
    form = todo_forms(request.POST or None, request.FILES, instance=idd)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'idd': idd})



