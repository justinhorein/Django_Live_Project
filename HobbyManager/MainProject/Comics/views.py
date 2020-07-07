from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Books  # import the class of Book to be able to use object definition
from .forms import ComicForm  # import the Book Form to be able to create and save


# View function that renders the home page
def comics_home(request):
    return render(request, 'Comics/Comics_home.html')


# First page for the comic book database
def index(request):
    get_comics = Books.Book.all()  # Gets all comics books in the collection database
    context = {'comics': get_comics}  # Creates a dictionary object for the books
    return render(request, 'Comics/Comics_index.html', context)


# View function to add a new book to the database
def add_book(request):
    form = ComicForm(request.POST or None)  # Gets the posted form, if one exists
    if form.is_valid():  # Checks the form for errors, to make sure it's filled in
        form.save()  # Saves the valid form and new comic to the database
        return redirect('listComics')  # Redirects to the index page, referenced in urls
    else:
        print(form.errors)  # Prints any errors for the posted form to the terminal
        form = ComicForm()  # Creates a new blank form
    return render(request, 'Comics/Comics_create.html', {'form': form})


# View function to look up the details of a book
def details_book(request, pk):
    pk = int(pk)  # Casts value of pk to an int so it's in the proper form
    books = get_object_or_404(Books, pk=pk)  # Gets single instance of the book from the database
    context = {'books': books}  # Creates dictionary object to pass the book object
    return render(request, 'Comics/Comics_details.html', context)


# View function to add a new book to the database
def post_edit(request, pk):
    post = get_object_or_404(Books, pk=pk)
    if request.method == "POST":
        form = ComicForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('bookDetails', pk=post.pk)
    else:
        form = ComicForm(instance=post)
    return render(request, 'Comics/Comics_edit.html', {'form': form})


def book_delete(request, pk):
    books = get_object_or_404(Books, pk=pk)
    if request.method == "POST":
        books.delete()
        return redirect('listComics')
    context = {'books': books}
    return render(request, "Comics/Comics_delete.html", context)


