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


import pytz

from django.contrib.auth import get_user_model
from django.utils.timezone import get_default_timezone
from fitparse.base import FitFile
from .models import Workout, Lap, Record

from fitparse.processors import StandardUnitsDataProcessor

import logging
logger = logging.getLogger(__name__)


class FullDatetimeProcessor(StandardUnitsDataProcessor):
    def process_type_date_time(self, field_data):
        super(FullDatetimeProcessor, self).process_type_date_time(field_data)
        if field_data.value and field_data.value.tzinfo is None:
            field_data.value = field_data.value.replace(tzinfo=pytz.UTC)


def importfitfile(f, user=None):
    if user is None:
        user = get_user_model().objects.all()[0]
    logger.info(u"Processing '%s'..." % f)
    fitfile = FitFile(
        f,
        data_processor=FullDatetimeProcessor(),
        check_crc=False
    )
    workout = Workout()
    logger.info(u"Processing session")
    for msg in fitfile.get_messages(name='session', as_dict=True):
        logger.debug(u"Session fields: %s" % str(msg['fields']))
        for f in msg['fields']:
            #if f['name'] == 'timestamp':
                #workout.title = f['value'].astimezone(get_default_timezone()).isoformat()
            if f['name'] == 'start_time':
                workout.publish_date = f['value']
                workout.title = f['value'].astimezone(get_default_timezone()).isoformat()
            if hasattr(workout, f['name']):
                setattr(workout, f['name'], f['value'])

    workout.user = user
    workout.save()

    logger.info(u"Processing laps")
    for msg in fitfile.get_messages(name='lap', as_dict=True):
        logger.info(" Lap: '%s'" % msg['name'])
        lap = Lap(workout=workout)
        for f in msg['fields']:
            if hasattr(lap, f['name']):
                setattr(lap, f['name'], f['value'])
        lap.save()

    logger.info(u"Processing data points")
    for msg in fitfile.get_messages(name='record', as_dict=True):
        record = Record(workout=workout)
        for f in msg['fields']:
            if hasattr(record, f['name']):
                setattr(record, f['name'], f['value'])
        record.save()

    logger.info("Finished.")
    return workout
