from django.shortcuts import render
from django.http import HttpResponse  # Keep this for index2 function
from .models import Book
from django.db.models import Q
from django.db.models import Avg, Max, Min, Sum, Count
from .models import Student, Address
from django.db.models import Count


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
def simple_query(request):
    # Query to find books with 'and' in their title (case-insensitive)
    books = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/simple_query.html', {'books': books})

def complex_query(request):
    # Query for books matching the conditions
    books = Book.objects.filter(
        author__isnull=False,       # Author name is not null
        title__icontains='and',    # Title contains 'and'
        edition__gte=2             # Edition is greater than or equal to 2
    ).exclude(
        price__lte=100             # Exclude books with price <= 100
    )[:10]                         # Limit results to 10 books

    # Render the results in a template
    return render(request, 'bookmodule/complex_query.html', {'books': books})

def task1(request):
    # Use Q operator to filter books with price <= 50
    books = Book.objects.filter(price__lte=50)
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    # Use Q operator for complex queries
    books = Book.objects.filter(
        Q(price__gte=100) | Q(edition=3),  # Price >= 100 OR Edition = 3
        author__isnull=False               # Author is not null
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    # Order books by price (ascending)
    books = Book.objects.order_by('price')  # Use '-price' for descending order
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    # Order books by title
    books = Book.objects.order_by('title')  # Ascending order
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5(request):
    # Perform aggregation on the Book model
    stats = Book.objects.aggregate(
        total_books=Count('id'),        # Total number of books
        total_price=Sum('price'),       # Total price of all books
        avg_price=Avg('price'),         # Average price
        max_price=Max('price'),         # Maximum price
        min_price=Min('price')          # Minimum price
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def task6(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/task6.html', {'students': students})


def task7(request):
    # Aggregate the number of students for each city
    students_per_city = Address.objects.annotate(student_count=Count('students'))
    return render(request, 'bookmodule/task7.html', {'students_per_city': students_per_city})
