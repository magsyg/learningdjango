from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

@login_required
def register(request):
    if (request.method == 'POST'):
        form = forms.WorkoutForm(request.POST)
        if(form.is_valid()):
            o = form.save(commit=False)
            o.user = request.user
            o.save()
            return redirect('landing')
    else:
        form = forms.WorkoutForm()
    return render(request, 'trening/create_trening.html',{'form': form})
