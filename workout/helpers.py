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

from fitparse.processors import StandardUnitsDataProcessor


class FullDatetimeProcessor(StandardUnitsDataProcessor):
    def process_type_date_time(self, field_data):
        super(FullDatetimeProcessor, self).process_type_date_time(field_data)
        if field_data.value and field_data.value.tzinfo is None:
            field_data.value = field_data.value.replace(tzinfo=pytz.UTC)
