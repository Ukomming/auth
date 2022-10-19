from django.shortcuts import render
from .form import RegisterForm

# Create your views here.
def home(request):
    return render(request, 'base.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    context={"form": form}
    return render(request, 'registration/sign_up.html',context)