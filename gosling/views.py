from django.shortcuts import render


def policy(request):
    return render(request, 'policy.html', {'panel': 2})


def about(request):
    return render(request, 'about.html')

