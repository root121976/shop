from django.shortcuts import render
from .forms import SubscriberForm

def landing(request):
    name = "KORENB76"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST":
        print (request.POST)
        new_form = form.save()

    return render(request,'landing.html', locals())
