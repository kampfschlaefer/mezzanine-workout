# Create your views here.

from django.views.generic import ListView, DetailView
from mezzanine.utils.views import render, paginate

from .models import Workout


class WorkoutList(ListView):
    model = Workout


class WorkoutDetail(DetailView):
    model = Workout
