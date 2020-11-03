from django.urls import path
from contact.views import contact_form, contact_sent

urlpatterns = [
    path("", contact_form, name="contact_form"),
    path("sent/", contact_sent, name="contact_sent"),
]