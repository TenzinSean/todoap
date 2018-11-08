from django.shortcuts import render
#from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import TodoItme


# Create your views here.
def HomePageView(request):
    all_todo_items = TodoItme.objects.all()
    return render(request, 'home.html',
        {'all_items': all_todo_items})


def addTodo(request):
    c = request.POST['content']
    new_item = TodoItme(content = c)
    new_item.save()
    return HttpResponseRedirect('/home/')
    # create a new # TODO:
    # save
    #redirect bowser

def deleteTodo(request,todo_id):
    item_to_delete = TodoItme.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/home/')
