from django.forms import CharField
from .widgets import TypeaheadTextInput

class TypeaheadCharField(CharField):

    def __init__(self, max_length=None, min_length=None, local="", prefetch="", prefetch_ttl=1440, remote="", attrs=None, *args, **kwargs):

        super(TypeaheadCharField, self).__init__(
            max_length=max_length, min_length=min_length,
            widget=TypeaheadTextInput(local=local, prefetch=prefetch, prefetch_ttl=prefetch_ttl, remote=remote, attrs=attrs),
            *args, **kwargs
        )