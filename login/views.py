from django.shortcuts import render
# login view
def login(request):
    return render(request, 'login/login.html')