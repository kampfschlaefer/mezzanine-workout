from django.db import models
from mezzanine.core.models import Displayable, Ownable, RichText


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
    @models.permalink
    def get_absolute_url(self):
        return ('workout_detail', (), {'pk': self.id}) #{'timestamp': self.publish_date.isoformat()})

    class Meta:
        ordering = ['-publish_date']


class Lap(AbstractLap):
    workout = models.ForeignKey(Workout, related_name='laps')


class Record(AbstractRecord):
    workout = models.ForeignKey(Workout, related_name='records')
