from django.shortcuts import render
from .models import Book
from datetime import datetime
from .forms import BookForm


# Create your views here.


def books(request):
    # Book.objects.filter(author__first_name="John"))
    context = {
        "books": Book.objects.all(),
        "date": datetime.now(),
        "form": BookForm
    }
    return render(request, "books.html", context)
