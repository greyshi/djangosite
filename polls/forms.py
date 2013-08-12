from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class PollForm(forms.Form):
    question = forms.CharField(
        label='Question',
        max_length=100
    )

    choice1 = forms.CharField(
        label='Choice',
        max_length=100
    )

    choice2 = forms.CharField(
        label='Choice',
        max_length=100
    )

    choice3 = forms.CharField(
        label='Choice',
        max_length=100,
        required=False
    )

    choice4 = forms.CharField(
        label='Choice',
        max_length=100,
        required=False
    )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('question', css_class='input-lg form-control', placeholder='Enter Question', style='margin-bottom: 20px'),
        Field('choice1', css_class='form-control', placeholder='Enter Choice', style='margin-bottom: 10px'),
        Field('choice2', css_class='form-control', placeholder='Enter Choice', style='margin-bottom: 10px'),
        Field('choice3', css_class='form-control', placeholder='Enter Choice', style='margin-bottom: 10px'),
        Field('choice4', css_class='form-control', placeholder='Enter Choice', style='margin-bottom: 10px'),
        FormActions(
            Submit('save_changes', 'Create', css_class="btn-primary btn-lg", style="margin-top: 10px"),
        )
   )
