from django.shortcuts import render, render_to_response

def isValid(email , password):
        return True

def index(request):
	return render(request, 'index.html')


def login(request):
        
        state = False
        
        if request.method == "POST":
                email = request.POST['email']
                password = request.POST['password']

                if isValid(email , password):
                        state = True
                        
        
        return render(request, 'login.html', {'state': state })

