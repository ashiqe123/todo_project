from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Todo
from .forms import Todo_forms
# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class classview(ListView):
    model=Todo
    template_name = 'home.html'
    context_object_name = 'key'
class detailview(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'key'

class updateview(UpdateView):
    model = Todo
    template_name = 'edit.html'
    context_object_name = 'key'
    fields = ('reminder','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdet',kwargs={'pk':self.object.id})


class deleteview(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')




















def home(request):
    todo1=Todo.objects.all()

    if request.method=='POST':
        reminder=request.POST.get('reminder')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        todo=Todo(reminder=reminder,priority=priority,date=date)
        todo.save()
    return render(request,'home.html',{'key':todo1})

def detail(request):
    todo=Todo.objects.all()
    return render(request,'detail.html',{'key':todo})

def delete(request,task_id):
    todo=Todo.objects.get(id=task_id)
    if request.method=='POST':
        todo.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):

    todo=Todo.objects.get(id=id)
    fm=Todo_forms(request.POST or None,instance=todo)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    return render(request,'update.html',{'todo':todo,'fm':fm})

