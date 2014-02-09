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

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
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
    list_display = ['publish_date', 'title', 'user', 'distance', 'total_time', 'speed', 'heartrate', 'categorylist', 'status', 'admin_link']
    list_per_page = 25
    actions = ['masscategories']

    def distance(self, instance):
        if instance.total_distance is not None:
            return '%.1f km' % (instance.total_distance/1000.)
        return ''

    def total_time(self, instance):
        if instance.total_timer_time is not None:
            seconds = instance.total_timer_time
            minutes = seconds // 60
            hours = minutes // 60
            return "%i:%02i:%02i" % (hours, minutes%60, seconds%60)

    def speed(self, instance):
        if instance.avg_speed is not None:
            return '%.1f km/h' % (instance.avg_speed*1000/360)
        return ''

    def heartrate(self, instance):
        if instance.avg_heart_rate is not None:
            return '%i bpm' % instance.avg_heart_rate
        return ''

    def categorylist(self, instance):
        return u', '.join([ cat.title for cat in instance.categories.all() ])

    def masscategories(self, request, queryset):
        return HttpResponseRedirect(
            "%s?wid=%s" % (
                reverse('workout_admin_masscategories'),
                '&wid='.join([ '%i' % w.id for w in queryset ])
            )
        )


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
