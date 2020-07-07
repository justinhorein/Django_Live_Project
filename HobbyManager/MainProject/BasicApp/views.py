import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import TravelList
from .forms import TravelForm


# Create your views here.


def basic_app_home(request):
    return render(request, 'BasicApp/BasicApp_home.html')

def index(request):
    get_trips = TravelList.TravelLists.all()
    context = {'TravelLists': get_trips}
    return render(request, 'BasicApp/BasicApp_index.html', context)


# View function to add
def add_travel(request):
    form = TravelForm(request.POST or None)  # Gets the posted form, if one exists
    if form.is_valid():  # Checks the form for errors, to make sure it's filled in
        form.save()  # Saves the valid form to the database
        return redirect('travelLists')  # Redirects to the index page
    else:
        print(form.errors)  # Prints any errors for the posted form to the terminal
        form = TravelForm()  # Creates a new blank form
    return render(request, 'BasicApp/BasicApp_create.html', {'form': form})


# View function to look up the details
def details(request, pk):
    pk = int(pk)  # Casts value of pk to an int so it's in the proper form
    trip = get_object_or_404(TravelList, pk=pk)  # Gets single instance from the database
    context = {'TravelList': trip}  # Creates dictionary object to pass the object
    return render(request, 'BasicApp/BasicApp_details.html', context)
