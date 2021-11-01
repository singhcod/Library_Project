from django.db import models
from django.contrib.auth.models import AbstractUser

class BookModel(models.Model):
    book_name = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30)
    pages = models.IntegerField()
    prise = models.FloatField()
    released_date = models.DateField(max_length=31)



    def __str__(self):
        return self.book_name


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.username


