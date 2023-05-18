from django.template import Library
from home.models import Categorie
from home.forms import SubcribeForm

register = Library()

@register.simple_tag
def global_categories():
    categories = Categorie.objects.all()
    return categories


@register.simple_tag
def global_form():
    form = SubcribeForm()
    return form