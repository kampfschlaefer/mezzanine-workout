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

from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import Displayable, Ownable, RichText, Slugged


class WorkoutCategory(Slugged):
    """
    A category for workouts. Heavily inspired by the categories in
    mezzanine.blog.
    """

    class Meta:
        verbose_name = _('Workout Category')
        verbose_name_plural = _('Workout Categories')
        ordering = ('title',)

    @models.permalink
    def get_absolute_url(self):
        return ('workout_list', (), {'category': self.slug})


# Create your models here.
class AbstractRecord(models.Model):
    altitude = models.FloatField(null=True, blank=True)
    #cadence: None [rpm]
    distance = models.FloatField(null=True, blank=True)
    #grade: None [%]
    heart_rate = models.FloatField(null=True, blank=True)
    position_lat = models.FloatField(null=True, blank=True)
    position_long = models.FloatField(null=True, blank=True)
    #power: None [watts]
    #resistance: None
    speed = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class AbstractLap(models.Model):
    avg_heart_rate = models.FloatField(null=True, blank=True)
    avg_speed = models.FloatField(null=True, blank=True)
    max_heart_rate = models.FloatField(null=True, blank=True)
    max_speed = models.FloatField(null=True, blank=True)
    total_ascent = models.FloatField(null=True, blank=True)
    total_calories = models.FloatField(null=True, blank=True)
    #total_descent: None [m]
    total_distance = models.FloatField(null=True, blank=True)
    total_elapsed_time = models.FloatField(null=True, blank=True)
    #total_fat_calories: None [kcal]
    #total_strides: None [strides]
    total_timer_time = models.FloatField(null=True, blank=True)

    start_position_lat = models.FloatField(null=True, blank=True)
    start_position_long = models.FloatField(null=True, blank=True)
    end_position_lat = models.FloatField(null=True, blank=True)
    end_position_long = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True


class Workout(AbstractLap, Displayable, Ownable, RichText):
    categories = models.ManyToManyField('WorkoutCategory',
                                        verbose_name=_('Workout Categories'),
                                        blank=True, related_name='workouts')

    @models.permalink
    def get_absolute_url(self):
        return ('workout_detail', (), {'pk': self.id})

    class Meta:
        ordering = ['-publish_date']


class Lap(AbstractLap):
    workout = models.ForeignKey(Workout, related_name='laps')


class Record(AbstractRecord):
    workout = models.ForeignKey(Workout, related_name='records')

    class Meta:
        ordering = ['timestamp']
