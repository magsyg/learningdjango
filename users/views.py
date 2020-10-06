from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if (request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('landing')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})