from django.urls import path
from .views import MealListView, MealCreateView, UserMealListView
from . import views

urlpatterns = [
    path('', MealListView.as_view(), name='diet-home'),
    path('new/', MealCreateView.as_view(), name='diet-create'),
    path('<str:username>', UserMealListView.as_view(), name='user-diet'),
]
