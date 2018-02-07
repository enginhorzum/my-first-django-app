
from django.urls import path, re_path
from customer.views import home, SignUpView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name="customer_home"),
    path('login', LoginView.as_view(template_name="customer/login_form.html"), name="customer_login"),
    path('logout', LogoutView.as_view(), name="customer_logout"),
    path('signup', SignUpView.as_view(), name="customer_signup")
]