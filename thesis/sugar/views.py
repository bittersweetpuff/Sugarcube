from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from .models import SugarLevel
from .interpreter import GenerateTrend, GenerateWarning



class SugarListView(ListView):
    model = SugarLevel
    template_name= 'sugar/home.html'
    context_object_name = 'sugars'
    ordering = ['-time']
    paginate_by = 5

class UserSugarListView(ListView):
    model = SugarLevel
    template_name = 'sugar/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'sugars'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return SugarLevel.objects.filter(owner=user).order_by('-time')
        #return SugarLevel.objects.filter(owner=user).latest()


class SugarCreateView(CreateView):
    model = SugarLevel
    fields = ['sugarlevel']

    def form_valid(self, form):
        u = self.request.user
        query = SugarLevel.objects.filter(owner=u).order_by('-time')
        latest = query.values().first()
        if query:
            form.instance.trend = GenerateTrend(latest['sugarlevel'], form.instance.sugarlevel, SugarLevel.objects.filter(owner=u).order_by('-time').first().get_time_diff())
        else:
            form.instance.trend = "Stabilny"

        form.instance.warning = GenerateWarning(form.instance.sugarlevel ,form.instance.trend)
        form.instance.owner = u
        return super().form_valid(form)


def about(request):
    return render(request, 'sugar/about.html', {'title': 'About'})
