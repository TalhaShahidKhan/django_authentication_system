from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from authentication.forms import RegistrationForm
from django.contrib.auth import login
# Create your views here.
def homepage(request):
  return render(request, 'main/index.html')
@login_required(login_url='/auth/login/')
def dashboardpage(request):
  return render(request, 'main/dashboard.html')

def signuppage(request):
  form=RegistrationForm()
  if request.method == "POST":
    form=RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form=RegistrationForm()
  context={
    "form":form
  }
  return render(request, 'registration/signup.html',context)