from django.shortcuts import render, redirect

def welcome(request):
    if request.user.is_authenticated:
        return redirect("customer_home")
    else:
        return render(request, "first-django-app/welcome.html")
