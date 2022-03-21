from django.shortcuts import render

def index(request):
    context ={
        'dan':True,
    }
    return render(request, 'index.html', context)
