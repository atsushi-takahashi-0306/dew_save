from django import forms
from .models import Wine





class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ['name', 'sort', 'country', 'vintage', 'grape', 'eye', 'nose', 'mouth','date', 'memo','point', 'pic']
    def __init__(self, *args, **kwargs):
        super(WineForm, self).__init__(*args, **kwargs)
        self.fields['name'].error_messages = {'required': 'こちらの項目は必須項目です。'}
        self.fields['sort'].error_messages = {'required': 'こちらの項目は必須項目です。'}
        self.fields['country'].error_messages = {'required': 'こちらの項目は必須項目です。'}
        self.fields['point'].error_messages = {'required': 'こちらの項目は必須項目です。'}