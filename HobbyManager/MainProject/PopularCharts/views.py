from django.shortcuts import render, redirect, get_object_or_404
from .models import Song
from .forms import SongForm

from django.http import HttpResponse


# View function that renders the home page - no context needed
def home(request):
    return render(request, 'PopularCharts/charts_home.html')

# First page for the song database
def index(request):
    get_songs = Song.Songs.all()  # Gets all songs in the database
    context = {'Song': get_songs}  # Creates a dictionary object for the songs
    return render(request, 'PopularCharts/index.html', context)

# View function that controls the ChartForm
def add_song(request):
    form = SongForm(request.POST or None)  # Gets the posted form, if one exists
    if form.is_valid():  # Checks the form for errors, to make sure it's filled in
        form.save()  # Saves the valid song details to the database
        return redirect('song_index')  # Redirects to the index page
        print(form.errors)  # Prints any errors for the posted form to the terminal
        form = SongForm()  # Creates a new blank form
    return render(request, 'PopularCharts/add_song.html', {'form': form})

# View function to look up the details of a song
def details_song(request, pk):
    pk = int(pk)  # Casts value of pk to an int so it's in the proper form
    song = get_object_or_404(Song, pk=pk)  # Gets single instance of the song from the database
    context = {'song': song}  # Creates dictionary object to pass the song object
    return render(request, 'PopularCharts/charts_details.html', context)