from django.shortcuts import render
from django.http import HttpResponse  # Keep this for index2 function

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):
    try:
        val1 = int(val1)  # Try to convert the input to an integer
        return HttpResponse(f"value1 = {val1}")
    except ValueError:
        return HttpResponse("Error, expected val1 to be an integer")  # Handle non-integer input
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
