from django import forms
from .models import AirlinesRefTable, AirportsRefTable, Dephour, Month, Monthday, Weekday, routes, SavedSearches
from django.db import connection, transaction
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, MultiField, Div
import datetime
from lookups import AirportsLookup
import selectable.forms as selectable

class InputForm(forms.Form):
    origin_airport = selectable.AutoCompleteSelectField(label = "Origin Airport", lookup_class=AirportsLookup, required=False)
    destination_airport = selectable.AutoCompleteSelectField(label = "Destination Airport", lookup_class=AirportsLookup, required=False)
    airline = forms.ModelChoiceField(queryset=AirlinesRefTable.objects.all(),required=False)
    dep_hour = forms.ModelChoiceField(queryset=Dephour.objects.all(), label = "Departure Time Block",required=False)
    month = forms.ModelChoiceField(queryset=Month.objects.all(), required=False)
    monthday = forms.ModelChoiceField(queryset=Monthday.objects.all(), label="Day of Month", required=False)
    weekday = forms.ModelChoiceField(queryset=Weekday.objects.all(), label="Weekday (Instead of Day of Month)", required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'container form-signin'
        self.helper.add_input(Submit('submit', 'Submit',css_class="container btn btn-lg btn-primary btn-block"))
        self.helper.layout = Layout(Div(Field('origin_airport',placeholder="Search by Airport name or Code"), Field('destination_airport',placeholder="Search by Airport name or Code"),
        Field('airline'), Field('dep_hour'), Field('month'), Field('monthday')),
        Div(Field('weekday')))

        super(InputForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(InputForm,self).clean()
        origin = cleaned_data.get("origin_airport")
        #origin_air = AirportsRefTable.objects.filter(unique_airport_id = origin)
        destination = cleaned_data.get("destination_airport")
        #destination_air = AirportsRefTable.objects.filter(unique_airport_id = destination)
        airline = cleaned_data.get("airline_airport")
        month = cleaned_data.get("month")
        monthday = cleaned_data.get("monthday")
        if origin and destination:
            check = routes.objects.filter(origin_airport=origin.unique_airport_id,dest_airport = destination.unique_airport_id)
            if len(check) == 0:
                origin_airport = None
                destination_airport = None
                raise forms.ValidationError("That direct route between airports does not exist, please select another")
        if origin and destination and airline:
            check = routes.objects.filter(airlineid = airline.airline_id_id,origin_airport=origin_airport.unique_airport_id,dest_airport = destination_airport.unique_airport_id)
            if len(check) == 0:
                airline = None
                origin_airport = None
                destination_airport = None
                raise forms.ValidationError("That direct route between airports does not exist for that airline, please select another")
        if month and monthday:
            if monthday.monthday > month.totaldays:
                raise forms.ValidationError("The Month and Day selected is not a valid date")
        return cleaned_data

class UserCreationForm(UserCreationForm):
    username = forms.RegexField(label='',max_length=30,regex=r'^[\w.@+-]+$',
        error_messages={'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password1 = forms.CharField(label='',widget=forms.PasswordInput,)
    password2 = forms.CharField(label='',widget=forms.PasswordInput,)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'container form-signin'
        self.helper.add_input(Submit('submit', 'Submit',css_class="container btn btn-lg btn-primary btn-block"))
        self.helper.layout = Layout(Div(Field('username', placeholder='Username'),
            Field('password1', placeholder='Password'),
            Field('password2', placeholder='Confirm Password')))

        super(UserCreationForm, self).__init__(*args, **kwargs)

class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label='')
    password = forms.CharField(label='', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'container form-signin'
        self.helper.add_input(Submit('submit', 'Submit',css_class="container btn btn-lg btn-primary btn-block"))
        self.helper.layout = Layout(Div(Field('username', placeholder='Username'),
            Field('password', placeholder='Password')))

        super(AuthenticationForm, self).__init__(*args, **kwargs)

class SaveSearchForm(forms.Form):
    search_name = forms.CharField(required=True, max_length=30,label='')

    def __init__(self, *args, **kwargs):
        #self.request = kwargs.pop('request', None)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '/savesearch/'
        self.helper.form_class = 'container form-signin'
        self.helper.add_input(Submit('submit', 'Submit',css_class="container btn btn-lg btn-primary btn-block"))
        self.helper.layout = Layout(Div(Field('search_name', placeholder='Search Name')))

        super(SaveSearchForm, self).__init__(*args, **kwargs)