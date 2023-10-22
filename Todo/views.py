from django.shortcuts import render, redirect
from .models import Note
from .forms import TodoForm

# Create your views here.
def Index(request):
    ItemList = Note.objects.order_by("-Date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Todo")
    form = TodoForm()
    page = {
        "forms":form,
        "List":ItemList,
        "title":"TodoList"
    }

    return render(request, './index.html', page)