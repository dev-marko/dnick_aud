from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    def __init__(self):
        super(BookForm, self).__init__()
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = 'form-control'

    class Meta:
        model = Book
        exclude = ("content",)
