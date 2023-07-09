from django.shortcuts import render
from .forms import ApplicationForm


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date_avail = form.cleaned_data["date_avail"]
            occupation = form.cleaned_data["occupation"]
            print(first_name)
    return render(request, "index.html")