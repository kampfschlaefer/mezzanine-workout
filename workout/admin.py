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

from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin

from .models import Workout

print DisplayableAdmin.fieldsets

class WorkoutAdmin(DisplayableAdmin, OwnableAdmin):
    fieldsets = list(DisplayableAdmin.fieldsets) + [
        ('WorkoutData', {
            'fields': [
                'content',
                'avg_heart_rate', 'avg_speed',
                'max_heart_rate', 'max_speed',
                'total_ascent', 'total_calories', 'total_distance', 'total_elapsed_time', 'total_timer_time',
            ],
        })
    ]

admin.site.register(Workout, WorkoutAdmin)
