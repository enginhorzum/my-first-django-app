from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

@login_required
def home(request):
    return render(request,"customer/home.html")

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "customer/signup_form.html"
    success_url = reverse_lazy('customer_home')