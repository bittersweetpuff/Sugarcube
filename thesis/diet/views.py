from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Meal
from .interpreter import CalculateInsulinDose


class MealListView(ListView):
    model = Meal
    template_name= 'diet/home.html'
    context_object_name = 'meals'
    ordering = ['-time']
    paginate_by = 5

class UserMealListView(ListView):
    model = Meal
    template_name= 'diet/home.html'
    context_object_name = 'meals'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Meal.objects.filter(owner=user).order_by('-time')


class MealCreateView(CreateView):
    model = Meal
    fields = ['poziom_cukru', 'jednostka', 'weglowodany', 'bialka', 'tluszcze', 'wrazliwosc', 'przelicznik']

    def get_success_url(self):
        return reverse('diet-home')

    def form_valid(self, form):
        u = self.request.user
        form.instance.owner = u
        if form.instance.jednostka == 'g':
            form.instance.weglowodany = form.instance.weglowodany*5
            form.instance.bialka = form.instance.bialka*5
            form.instance.tluszcze = form.instance.tluszcze*9

        form.instance.kalorycznosc = form.instance.weglowodany + form.instance.bialka + form.instance.tluszcze
        interpret = CalculateInsulinDose(form.instance.weglowodany, form.instance.tluszcze, form.instance.bialka, form.instance.wrazliwosc, form.instance.przelicznik, form.instance.poziom_cukru)
        form.instance.insulin_dose = interpret["insulin_dose"]
        form.instance.bolus = interpret["bolus"]
        form.instance.warning = interpret["warning"]
        return super().form_valid(form)
