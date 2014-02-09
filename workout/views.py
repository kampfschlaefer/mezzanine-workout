#
#   Copyright 2013 by Arnold Krille <arnold@arnoldarts.de>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from mezzanine.utils.views import render, paginate

from .models import Workout
from .forms import FitFileImportForm, AdminMassCategoriesForm
from .helpers import importfitfile


class WorkoutList(ListView):
    model = Workout

    def get_queryset(self):
        return Workout.objects.published(for_user=self.request.user)


class WorkoutDetail(DetailView):
    model = Workout


class ImportFitView(FormView):
    form_class = FitFileImportForm
    success_url = '/workout/'
    template_name = 'workout/importfile.html'

    def form_valid(self, form):
        workout = importfitfile(self.request.FILES['uploadfile'], self.request.user)
        return HttpResponseRedirect(reverse('workout_detail', args=[workout.id]))


class GraphOverview(ListView):
    template_name = 'workout/graphoverview.html'

    def get_queryset(self):
        return Workout.objects.published(for_user=self.request.user).order_by('publish_date')


class AdminMassCategory(FormView):
    form_class = AdminMassCategoriesForm
    template_name = 'workout/admin_mass_categories.html'

    def get_initial(self):
        print "get_initial!"
        return {
            'workouts': ','.join(
                [ s for s in self.request.GET.getlist('wid')]
            )
         }

    def form_valid(self, form):
        print "form_valid!"
        for wid in form.cleaned_data['workouts'].split(','):
            w = Workout.objects.get(pk=wid)
            w.categories.add(form.cleaned_data['category'])
        return HttpResponseRedirect(reverse('admin:workout_workout_changelist'))
