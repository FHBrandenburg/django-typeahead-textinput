from django.http import HttpResponse
from django.template import RequestContext, loader
from testapp.models import Author
from testapp.forms import AuthorForm
from django.contrib import messages
from jsonview.decorators import json_view

def index(request):
    author = Author()

    if request.method=='POST':
        # Formular wurde abgeschickt
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, u"Author saved successfully.")
            #return HttpResponseRedirect(reverse('wherever'))
        else:
            messages.error(request, u"Data incorrect.")
            pass
    else:
        form = AuthorForm(instance=author)

    template = loader.get_template('testapp/testpage.html')
    context = RequestContext(request, {'form':form})
    return HttpResponse(template.render(context))

@json_view
def json_towns(request):
    return list(set([a.town for a in Author.objects.all()]))
