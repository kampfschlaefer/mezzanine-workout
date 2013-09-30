
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.utils.timezone import get_default_timezone
from fitparse.base import FitFile

from ...models import Workout, Lap, Record
from ...helpers import FullDatetimeProcessor

class Command(BaseCommand):
    args = '<fitfile> ...'
    help = u'Import FIT-files from garmin devices into workout-data'

    def handle(self, *args, **options):
        print "Should import files from %s" % list(args)
        for f in args:
            print "Processing '%s'..." % f
            fitfile = FitFile(
                f,
                data_processor=FullDatetimeProcessor(),
                check_crc=False
            )
            #print fitfile
            workout = Workout()
            print "  Processing session"
            for msg in fitfile.get_messages(name='session', as_dict=True):
                print msg['fields']
                for f in msg['fields']:
                    if f['name'] == 'timestamp':
                        workout.title = f['value'].astimezone(get_default_timezone()).isoformat()
                    if f['name'] == 'start_time':
                        workout.publish_date = f['value']
                    if hasattr(workout, f['name']):
                        print "   Setting '%s' to '%s'" % (f['name'], f['value'])
                        setattr(workout, f['name'], f['value'])

            workout.user = get_user_model().objects.all()[0]
            workout.save()

            print "  Processing laps"
            for msg in fitfile.get_messages(name='lap', as_dict=True):
                print msg['name']
                lap = Lap(workout=workout)
                for f in msg['fields']:
                    if hasattr(lap, f['name']):
                        getattr(lap, f['name'], f['value'])
                lap.save()

            print "  Processing data points"
            for msg in fitfile.get_messages(name='record', as_dict=True):
                record = Record(workout=workout)
                for f in msg['fields']:
                    if hasattr(record, f['name']):
                        setattr(record, f['name'], f['value'])
                record.save()

            print " Finished."
