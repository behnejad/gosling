from django.shortcuts import render, render_to_response


def index(request):
	return render(request, 'index.html')



def login(request):
	return render(request, 'index.html')



def logout(request):
	return render(request, 'index.html')



def password_change(request):
	return render(request, 'index.html')



def password_change_done(request):
	return render(request, 'index.html')



def password_reset(request):
	return render(request, 'index.html')



def password_reset_done(request):
	return render(request, 'index.html')


def password_reset_complete(request):
	return render(request, 'index.html')


