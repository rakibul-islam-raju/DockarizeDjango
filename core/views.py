from django.shortcuts import render


def hello_docker(request):
    return render(request, 'index.html')
