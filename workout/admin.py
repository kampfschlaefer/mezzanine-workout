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
