from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from contact.forms import Contact


def contact_form(request):
    '''
    Takes in POST and GET requests for the contact form page.
    If a contact form was submitted:
        1. Extract submitted information from a new Contact instance
        2. Send message to vxjian@seas.upenn.edu (if all valid fields)
        3. Redirect to success page
    Otherwise, display template with blank form.
    args:
        request: the contact form request
    ret: Renders the correct page depending on the request
    '''
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, from_email, ['vxjian@seas.upenn.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_sent')
    else:
        form = Contact()
    return render(request, "contact_form.html", {'form': form})


def contact_sent(request):
    '''
    Displays the "sent" template after a user submits a contact form.
    '''
    return render(request, 'contact_sent.html')
