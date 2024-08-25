from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publication_year')	# Displays the listed fields
	search_fields = ('title', 'author')	# Search Parameters
	list_filter = ('publication_year',)	# Filter for publication year

# Register the Book model with the Django admin
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
	model = CustomUser
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('date_of_birth', 'profile_photo')}),
	)
	add_fieldsets = UserAdmin.add_fieldsets + (
		(None, {'fields': ('date_of_birth', 'profile_photo')}),
	)

admin.site.register(CustomUser, CustomUserAdmin)