from django.contrib import admin
from .models import BookModel
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class BooksAdmin(admin.ModelAdmin):
    list_display = ('id','book_name','author_name','pages','prise','released_date')

admin.site.register(BookModel,BooksAdmin)





class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","email")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username","email")
