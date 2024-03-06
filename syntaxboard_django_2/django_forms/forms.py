from django import forms
import datetime
from . import formdata as fd


class TrainingForm(forms.Form):

    # Data
    form_choices = fd.form_choices
    form_choices1 = fd.form_choices1
    year_data =fd.year_data

    # HTML Controls
    # HTML INPUT Box
    userid = forms.CharField(initial="Enter User Name")
    passwd = forms.CharField( widget=forms.PasswordInput())

    # Date Control
    dateinput = forms.DateField( label='Enter Date: '
                                ,widget=forms.SelectDateWidget(years=year_data)
                                ,initial=datetime.date.today)



    # HTML Drop Down Box
    DropDownBox = forms.ChoiceField(choices=form_choices)

    # HTML Radio Buttons
    RadioButtons = forms.ChoiceField(choices=form_choices, widget=forms.RadioSelect)

    # HTML Multi Select Text Box
    MultiSelect = forms.MultipleChoiceField(choices=form_choices1)

    # HTML Check Box
    CheckBox = forms.MultipleChoiceField(choices=form_choices, widget=forms.CheckboxSelectMultiple)
