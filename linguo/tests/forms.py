from django import forms
from django.utils.translation import ugettext_lazy as _

from linguo.forms import MultilingualModelForm
from linguo.tests.models import Bar


class BarForm(forms.ModelForm):
    class Meta:
        model = Bar


class BarFormWithFieldsSpecified(forms.ModelForm):
    class Meta:
        model = Bar
        fields = ('name', 'price', 'description', 'quantity',)


class BarFormWithFieldsExcluded(forms.ModelForm):
    class Meta:
        model = Bar
        exclude = ('categories', 'name',)


class BarFormWithCustomField(BarFormWithFieldsSpecified):
    custom_field = forms.CharField(label=_('custom'))


class MultilingualBarFormAllFields(MultilingualModelForm):
    class Meta:
        model = Bar
