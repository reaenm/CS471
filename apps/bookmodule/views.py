from django.shortcuts import render
from django.http import HttpResponse  # Keep this for index2 function

# Existing view for the index page
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

# Existing view for index2, handling integers
def index2(request, val1=0):
    try:
        val1 = int(val1)  # Try to convert the input to an integer
        return HttpResponse(f"value1 = {val1}")
    except ValueError:
        return HttpResponse("Error, expected val1 to be an integer")  # Handle non-integer input

# Existing view for viewing a single book
def viewbook(request, bookId):
    # Simulate a list of books
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    # Find the book by its ID
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    # Pass the book to the template
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)

# Missing view functions
def links(request):
    return render(request, 'bookmodule/links.html')  # Use the links.html template

def formatting(request):
    return render(request, 'bookmodule/formatting.html')  # Use the formatting.html template

def listing(request):
    return render(request, 'bookmodule/listing.html')  # Use the listing.html template

def tables(request):
    return render(request, 'bookmodule/tables.html')  # Use the tables.html template

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')  # Use the aboutus.html template

def list_books(request):
    return render(request, 'bookmodule/list_books.html')  # Use the list_books.html template

def search_books(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        search_title = 'option1' in request.POST
        search_author = 'option2' in request.POST

        # Example list of books (replace with database queries if needed)
        books = [
            {'id': 1, 'title': 'Django Unleashed', 'author': 'Andrew Pinkham'},
            {'id': 2, 'title': 'Two Scoops of Django', 'author': 'Audrey Roy'},
            {'id': 3, 'title': 'Python Crash Course', 'author': 'Eric Matthes'},
        ]

        # Filter books based on the search criteria
        results = []
        for book in books:
            if (search_title and keyword in book['title'].lower()) or \
               (search_author and keyword in book['author'].lower()):
                results.append(book)

        return render(request, 'bookmodule/bookList.html', {'books': results})

    return render(request, 'bookmodule/search.html')
