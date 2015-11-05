from django.shortcuts import render, render_to_response


def index(request):
    return render(request, 'index.html')


def group(request):
    return render(request, 'index.html')


def list(request):
    return render(request, 'index.html')


def problems(request):
    return render(request, 'index.html')

