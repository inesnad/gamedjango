from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class ResultForm(forms.Form):
    score = forms.IntegerField(
        label='Score',
        required=True
        )
    #player = forms.ForeignKey(queryset=Player.objects.all())

    def clean_score(self):
        data = self.cleaned_data['score']
        
        #Check score is not negative. 
        if data < 0 :
            raise ValidationError(_('Invalid score'))

        # Remember to always return the cleaned data.
        return data
