from django.shortcuts import render, redirect
from .models import Test
from .forms import TestForm



def home(request):
    tests = Test.objects.all()
    return render(request, 'home.html', context={'tests' : tests})


def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'create_test.html', context={'form':TestForm()})


def detail_test(request, pk):
    test = Test.objects.get(id=pk)
    return render(request, 'test.html', context={'test': test})



def update_test(request, pk):
    test = Test.objects.get(id=pk)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'update_test.html', context={'form':TestForm(instance=test)})


def delete_test(request, pk):
    Test.objects.get(id=pk).delete()
    return redirect('home')






