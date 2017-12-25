from django.forms import ModelForm
from .models import Rant

class RantForm(ModelForm):
    class Meta:
        model = Rant
        fields = ("title", "body",)
