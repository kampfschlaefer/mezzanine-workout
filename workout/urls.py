
from django.conf.urls import patterns, url

from .views import WorkoutList, WorkoutDetail

urlpatterns = patterns('workout.views',
    url(r'^/$', WorkoutList.as_view(), ),
    url(r'/(?P<pk>\d+)', WorkoutDetail.as_view(), name='workout_detail'),
)
