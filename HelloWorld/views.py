from django.shortcuts import render, redirect
from .models import Book
from datetime import datetime
from .forms import BookForm


# Create your views here.


def books(request):
    # Book.objects.filter(author__first_name="John"))
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            # commit = false - sakame da ostavime moznost da moze da napravime
            # override na nekoi od polinjata vo formata
            book = form.save(commit=False)
            book.save()
            return redirect(books)
            # Vlatko vo aud dodade user pole vo book kade sto se cuva
            # tekovno logiraniot korisnik za da moze da gi vleceme
            # samo negovite knigi - ne mi se pravese toa whatever
            # book.user = request.user
            # book.save()
    context = {
        "books": Book.objects.all(),
        "date": datetime.now(),
        "form": BookForm
    }
    return render(request, "books.html", context)
