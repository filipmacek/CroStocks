from django.shortcuts import render
from django.views.generic.edit import FormView
from CroStocks import forms

def home_page(request):
    return render(request,'base.html')


class ContactUsView(FormView):
    template_name = "contact-us.html"
    form_class=forms.ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)

