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

from django import forms
from .models import WorkoutCategory

class FitFileImportForm(forms.Form):
    uploadfile = forms.FileField()


class AdminMassCategoriesForm(forms.Form):
    category = forms.ModelChoiceField(queryset=WorkoutCategory.objects.all())
    #workouts = forms.ModelMultipleChoiceField(widget=forms.MultipleHiddenInput())
    workouts = forms.CharField(max_length=200, widget=forms.HiddenInput)
