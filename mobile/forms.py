from django.forms import ModelForm
from django.forms import widgets

from mobile.models import Email


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email', 'message']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'email-field'}),
            'message': widgets.Textarea(attrs={'cols': 30, 'rows': 20, 'class': 'message-field'}),
        }
