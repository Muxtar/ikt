from django.shortcuts import render
from contact.models import Contact
from django.http import (   HttpResponse,
                            JsonResponse)

from contact.forms import ContactForm

# Create your views here.

def contact(request):
    form = ContactForm()
    context = {'form':form}
    if request.method == 'POST':
        test = ContactForm(request.POST)
        if test.is_valid():
            Contact.objects.create(name = test.cleaned_data['name'], email = test.cleaned_data['email'], subject = test.cleaned_data['subject'], messages = test.cleaned_data['messages'])
        else:
            context = {'form':test}

    return render(template_name='contact.html', request=request, context=context)
