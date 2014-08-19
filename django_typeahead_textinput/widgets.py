from django.forms import TextInput
from django.template.response import SimpleTemplateResponse

class TypeaheadTextInput(TextInput):
    def __init__(self, local="", prefetch="", prefetch_ttl=1440, remote="", attrs=None):
        super(TypeaheadTextInput, self).__init__(attrs=attrs)
        self.local = local
        self.prefetch = prefetch
        self.prefetch_ttl = prefetch_ttl
        self.remote = remote

    def render(self, name, value, attrs=None):
        output = super(TypeaheadTextInput, self).render(name=name, value=value, attrs=attrs,)
        if self.local != "":
            self.local = 'local: $.map('+self.local+', function(v) { return { value: v }; }),'

        if self.prefetch != "":
            self.prefetch = '''prefetch: {url: "'''+self.prefetch+'''",
                ttl: '''+str(self.prefetch_ttl*60000)+''',
                filter: function(list) {
                    return $.map(list, function(v) { return { value: v }; });
                }
            },'''

        if self.remote != "":
            self.remote = '''remote: {url: "'''+self.remote+'''",
                filter: function(list) {
                    return $.map(list, function(v) { return { value: v }; });
                }
            }'''

        stresponse = SimpleTemplateResponse("django_typeahead_textinput/typeahead-bloodhound-script.html",
                                            {"typeahead_name": "id_"+name,
                                             "typeahead_local": self.local,
                                             "typeahead_prefetch": self.prefetch,
                                             "typeahead_remote": self.remote})
        stresponse.render()
        output += stresponse.rendered_content
        return output

    class Media:
        css = {
            'all':
                ('django_typeahead_textinput/css/typeahead.css',)
        }
        js = (
            '//cdn.jsdelivr.net/typeahead.js/0.10.5/typeahead.bundle.min.js',
        )
