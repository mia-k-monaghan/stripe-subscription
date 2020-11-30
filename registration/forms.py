from django import forms
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
            'Account Information',
            Row(
                Column('first_name', css_class='form-group col-md-6'),
                Column('last_name', css_class='form-group col-md-6'),
            ),
            'email',
            'password1',
            'password2',
            )
        )
        self.helper.form_tag = False

class LoginForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
