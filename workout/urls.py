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


from django.conf.urls import patterns, url

from .views import WorkoutList, WorkoutDetail, ImportFitView, GraphOverview

urlpatterns = patterns('workout.views',
    url(r'^/$', WorkoutList.as_view(), ),
    url(r'^/graphs/$', GraphOverview.as_view(), name='workout_graphs'),
    url(r'^/importfile/$', ImportFitView.as_view(), name='workout_importfile'),
    url(r'^/(?P<pk>\d+)', WorkoutDetail.as_view(), name='workout_detail'),
)
