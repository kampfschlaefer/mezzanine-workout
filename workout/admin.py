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

from copy import deepcopy

from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin, OwnableAdmin
from mezzanine.conf import settings

from .models import Workout, WorkoutCategory

fieldsets = list(deepcopy(DisplayableAdmin.fieldsets))
fieldsets[0][1]['fields'].insert(1, 'categories')
fieldsets[0][1]['fields'].extend(['content'])
fieldsets.insert(1, (
    'Workout Data', {
        'fields': [
            'avg_heart_rate', 'avg_speed',
            'max_heart_rate', 'max_speed',
            'total_ascent', 'total_calories', 'total_distance',
            'total_elapsed_time', 'total_timer_time',
        ]
    }
))
list_filter = deepcopy(DisplayableAdmin.list_filter) + ('categories',)


class WorkoutAdmin(DisplayableAdmin, OwnableAdmin):
    fieldsets = fieldsets
    list_filter = list_filter


class WorkoutCategoryAdmin(admin.ModelAdmin):
    """
    Admin class for workout categories. Hides itself from the admin menu
    unless explicitly specified.
    """

    fieldsets = ((None, {"fields": ("title",)}),)

    def in_menu(self):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "workout.WorkoutCategory" in items:
                return True
        return False

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutCategory, WorkoutCategoryAdmin)
