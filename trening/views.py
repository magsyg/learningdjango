from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from . import forms
from users.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.

@login_required
def register(request):
    if (request.method == 'POST'):
        form = forms.WorkoutForm(request.POST)
        if(form.is_valid()):
            o = form.save(commit=False)
            o.user = request.user
            o.save()
            messages.success(request, 'Training Registered!')
            return redirect('landing')
    else:
        form = forms.WorkoutForm()
    return render(request, 'trening/create_trening.html',{'form': form})

class results(LoginRequiredMixin, TemplateView):
    template_name = 'trening/results.html'

    def get_context_data(self, **kwargs):
        ctx = super(results, self).get_context_data(**kwargs)
        ctx = {'t': {}}
        ctx['t']['header'] = ['Navn', 'Seksjon', 'Antall Økter', 'Total Distanse', 'Total Score']
        ctx['t']['rows'] = []
        for user in User.objects.all():
            row = {'Navn':user.username,
                                    'Seksjon':user.section,
                                    'Antall Økter':user.total_workouts(), 
                                    'Total Distanse':user.distance_sum(),
                                    'Total Score': user.score()}
            if user == self.request.user:
                row['marked'] = True
            else:
                row['marked'] = False

            ctx['t']['rows'].append(row)
        print(ctx)
        return ctx

    
