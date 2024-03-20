from django.forms import ModelForm
from django import forms
from config.models import UserConfig
from services.controler import MetaTraderControler



class CreateConfigUser(ModelForm):
    account = forms.CharField(required=False)
    password = forms.CharField(required=False)
    file_name = forms.CharField(required=False)
    server = forms.CharField(required=False)
    investor = forms.CharField(required=False)

    class Meta:
        model = UserConfig
        fields = ['account', 'password', 'file_name', 'investor', 'server']

    def is_valid(self):
        valid = super(CreateConfigUser,self).is_valid()
        authorize = MetaTraderControler(
            int(self.data['account']),
            self.data['password'],
            self.data['server'],
            self.data['file_name']
        ).check_authorize()
        if valid and authorize:
            return True
        return False
