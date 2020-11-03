from django import forms


class Contact(forms.Form):
    '''
    The contact form class, which leverages Django's built-in form class.
    Requires three fields:
     'from_email' (a user's email)
     'name' (the user's name)
     'message' (the user's message to be sent)
    '''
    from_email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        '''
        Configures the form to display updated field labels on the webpage.
        '''
        super(Contact, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Your name:"
        self.fields['from_email'].label = "Your email:"
        self.fields['message'].label = "Your message:"