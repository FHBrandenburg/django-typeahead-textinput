# Typeahead for Django CharFields/TextInput

## Requirements:
* __django-bootstrap3__ is not a strict requirement, but the included CSS file was made with bootstrap in mind
* __jQuery__ since Typeahead is a jQuery plugin

## Installation:
* pip install django-typeahead-textinput-0.2.zip

## Usage:
* Add `django_typeahead_textinput` to the installed applications in your settings.py
* Simply use a `TypeaheadCharField` instead of a regular `CharField` wherever you need autocomplete functionality
    * `from django_typeahead_textinput.fields import TypeaheadCharField`
* The same goes for a `TypeaheadTextInput` instead of a regular `TextInput`
    * `from django_typeahead_textinput.widgets import TypeaheadTextInput`
* `TypeaheadCharField` and `TypeaheadTextInput` take a few new parameters to set up the data source for Bloodhound:
    * `local` must be a string that contains a javascript array or the name of a variable that references one
    * `prefetch` and `remote` must be strings that contain the URLs of data in the JSON format
    * `prefetch_ttl` is the *time to live* of the prefetched data **in minutes** and must be an integer
    
* Make sure you insert jQuery at the top of your template
* Don't forget to place {{ form.media }} above your form

## Example:

Let's say you are building a simple application and one of your models is `Author`:

__models.py__

    class Author(models.Model):
        name = models.CharField(max_length=30)
        town = models.CharField(max_length=30)
        
You would like to create a form to add new authors to your database.
To do that, you use:

__forms.py__

    from django_typeahead_textinput.widgets import TypeaheadTextInput

    class AuthorForm(ModelForm):
        class Meta:
            model = Author
            widgets = {
                'town': TypeaheadTextInput(prefetch='/typeahead/json/towns', prefetch_ttl=60)
            }

To make adding authors easier, you want to provide autocomplete-functionality for the `town` field.
In this example, we are going to use prefetched data only.
If you had very large datasets in your database, you would want to use remote data.
You want your data to be cached for 60 **minutes**. 
`'/typeahead/json/towns'` is a reference to a dynamically generated JSON view of all your authors:

__views.py__

    @json_view
    def json_towns(request):
        return list(set([a.town for a in Author.objects.all()]))
        
After creating your actual view, you insert this into your template, just like you would for any other form:

__addauthor.html__

    {{ form.media }}

    <form action="" method="post">
        {% csrf_token %}
        {% bootstrap_form form layout="horizontal" %}
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    
Please note, how `{{ form.media }}` is placed _above_ the form.



