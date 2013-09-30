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

import logging

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.utils.timezone import get_default_timezone
from fitparse.base import FitFile

from ...models import Workout, Lap, Record
from ...helpers import FullDatetimeProcessor

class Command(BaseCommand):
    args = '<fitfile> ...'
    help = u'Import FIT-files from garmin devices into workout-data'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__+'.'+self.__class__.__name__)

    def handle(self, *args, **options):
        for f in args:
            self.logger.info(u"Processing '%s'..." % f)
            fitfile = FitFile(
                f,
                data_processor=FullDatetimeProcessor(),
                check_crc=False
            )
            workout = Workout()
            self.logger.info(u"Processing session")
            for msg in fitfile.get_messages(name='session', as_dict=True):
                self.logger.debug(u"Session fields: %s" % str(msg['fields']))
                for f in msg['fields']:
                    if f['name'] == 'timestamp':
                        workout.title = f['value'].astimezone(get_default_timezone()).isoformat()
                    if f['name'] == 'start_time':
                        workout.publish_date = f['value']
                    if hasattr(workout, f['name']):
                        setattr(workout, f['name'], f['value'])

            workout.user = get_user_model().objects.all()[0]
            workout.save()

            self.logger.info(u"Processing laps")
            for msg in fitfile.get_messages(name='lap', as_dict=True):
                self.logger.info(" Lap: '%s'" % msg['name'])
                lap = Lap(workout=workout)
                for f in msg['fields']:
                    if hasattr(lap, f['name']):
                        setattr(lap, f['name'], f['value'])
                lap.save()

            self.logger.info(u"Processing data points")
            for msg in fitfile.get_messages(name='record', as_dict=True):
                record = Record(workout=workout)
                for f in msg['fields']:
                    if hasattr(record, f['name']):
                        setattr(record, f['name'], f['value'])
                record.save()

            self.logger.info("Finished.")
