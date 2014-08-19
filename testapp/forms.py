from django.forms import *
from testapp.models import Author
from django_typeahead_textinput.widgets import TypeaheadTextInput


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        widgets = {
            'town': TypeaheadTextInput(prefetch='/typeahead/json/towns', prefetch_ttl=1)
        }