from django.shortcuts import render, render_to_response


def index(request):
    return render(request, 'index.html')


def exam(request):
    return render(request, 'index.html')


def exam_list(request):
    return render(request, 'index.html')


def group(request):
    return render(request, 'index.html')


def group_list(request):
    return render(request, 'index.html')


def problem(request):
    return render(request, 'index.html')

