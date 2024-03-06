from django import forms

class TestForm(forms.Form):
    # HTML INPUT Box
    userid = forms.CharField()

    form_choices = (
        (1, 'Food'),
        (2, 'Drinks'),
        (3, 'Cleaning Supplies'),
        (4, 'Body Care'),
        (5, 'House Ware'),
        (6, 'Electronics')
    )

    CheckBox = forms.MultipleChoiceField(choices=form_choices, widget=forms.CheckboxSelectMultiple)
