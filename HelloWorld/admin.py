from django.contrib import admin
from .models import Author, Book, Publication, PublicationAuthor


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "year_of_birth")
    list_filter = ("first_name", "year_of_birth")

    # Vakvoto ogranicuvanje na permisii e korisno koga imame
    # razlicni tipovi (roles) na korisnici

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)


class PublicationAuthorAdmin(admin.StackedInline):
    model = PublicationAuthor
    extra = 0


class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationAuthorAdmin, ]


admin.site.register(Publication, PublicationAdmin)