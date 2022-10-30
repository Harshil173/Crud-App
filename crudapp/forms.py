from django.forms import ModelForm
from .models import *

class SinfoForm(ModelForm):
    class Meta:
        model = sinfo
        fields = '__all__'
