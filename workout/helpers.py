
import pytz

from fitparse.processors import StandardUnitsDataProcessor


class FullDatetimeProcessor(StandardUnitsDataProcessor):
    def process_type_date_time(self, field_data):
        super(FullDatetimeProcessor, self).process_type_date_time(field_data)
        if field_data.value and field_data.value.tzinfo is None:
            field_data.value = field_data.value.replace(tzinfo=pytz.UTC)
