from django.shortcuts import render, redirect, get_object_or_404
from .forms import BeerForm
from .models import Beer


# View function that renders the home page - no context needed
def home(request):
    return render(request, 'CraftBeer/craftbeer_home.html')


# View function that controls the main index page - list of beers
def index(request):
    get_beers = Beer.beers.all()  # Gets all the current beers from the database
    context = {'beers': get_beers}  # Creates a dictionary object of all the beers for the template
    return render(request, 'CraftBeer/craftbeer_index.html', context)


# View function to add a new beer to the database
def add_beer(request):
    form = BeerForm(request.POST or None)  # Gets the posted form, if one exists
    if form.is_valid():  # Checks the form for errors, to make sure it's filled in
        form.save()  # Saves the valid form/beer to the database
        return redirect('listBeers')  # Redirects to the index page
    else:
        print(form.errors)  # Prints any errors for the posted form to the terminal
        form = BeerForm()  # Creates a new blank form
    return render(request, 'CraftBeer/craftbeer_create.html', {'form': form})


# View function to get details of a beer
def details_beer(request, pk):
    beer = get_object_or_404(Beer, pk=pk) # get beer record if it exists
    return render(request, 'CraftBeer/craftbeer_details.html', context={'beer': beer})


# View function to edit details of a beer
def edit_beer(request, pk):
    beer = get_object_or_404(Beer, pk=pk) # get beer record if it exists
    if request.method == "POST":
        form = BeerForm(request.POST, instance=beer)  # gets the posted form
        if form.is_valid():  # Checks the form for errors, to make sure it's filled in
            beer = form.save()  # Saves the valid form/beer to the database
            beer.save()
            return redirect('beerDetails', pk=beer.pk)
    else:
        form = BeerForm(instance=beer)
    return render(request, 'CraftBeer/craftbeer_edit.html', {'form': form})


# View function to delete a beer
def delete_beer(request, pk):
    beer = get_object_or_404(Beer, pk=pk)
    if request.method == "POST":
        beer.delete()
        return redirect('listBeers') # redirects to the index page
    return render(request, "CraftBeer/craftbeer_confirmdelete.html", context={'beer': beer})
