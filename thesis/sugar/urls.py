from django.urls import path
from .views import SugarListView, SugarCreateView, UserSugarListView
from . import views

urlpatterns = [
    path('', SugarListView.as_view(), name='sugar-home'),
    path('about/', views.about, name='sugar-about'),
    path('sugar/new/', SugarCreateView.as_view(), name='sugar-create'),
    path('sugar/<str:username>', UserSugarListView.as_view(), name='user-sugarlevel'),
]
