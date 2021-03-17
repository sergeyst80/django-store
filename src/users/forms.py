from django.contrib.auth import forms as auth_forms, models as auth_models
from django import forms
from users import models

class UserProfileExtForm(forms.ModelForm):
    class Meta:
        model = models.ExtUserData
        fields = ('phone', 'country', 'city', 'post_index', 'address1' ,'address2')
    
    # def __init__(self, *args, **kwargs):
    #     super(UserProfileExtForm, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['address1'].widget.attrs['disabled'] = 'disabled'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = auth_models.User
        fields = ('first_name', 'last_name', 'email')