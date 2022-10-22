from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models


# Create your models here.

class Reviews(models.Model):
    title_id = models.ForeignKey(Title, on_delete=CASCADE, blank=False)
    text = models.TextField(blank=False)

    class Scores(models.IntegerChoices):
        ONE = 1,
        TWO = 2,
        THREE = 3,
        FOUR = 4,
        FIVE = 5,
        SIX = 6,
        SEVEN = 7,
        EIGHT = 8,
        NINE = 9,
        TEN = 10

    score = models.IntegerField(null=False, choices=Scores.choices)
    author = models.ForeignKey(User, on_delete=CASCADE)
    pub_date = models.DateTimeField()


class Titles(models.Model):
    name = models.CharField(max_length=250, blank=False)
    year = models.IntegerField(blank=False)
    description = models.CharField()
    category = models.ForeignKey(Categories, on_delete=CASCADE, blank=FALSE)
    genre = models.ManyToManyField(Genres)


class Categories(models.Model):
    name = models.Charfield(max_lenght=256, blank=False)
    slug = models.SlugField(max_length=50, blank=False)


class Genres(models.Model):
    name = models.Charfield(max_lenght=256, blank=False)
    slug = models.SlugField(max_length=50, blank=False)


class Comments(models.Model):
    title_id = models.ForeignKey(Titles, on_delete=CASCADE)
    review_id = models.ForeignKey(Reviews, on_delete=CASCADE)
    text = models.CharField(blank=False)
    author = models.ForeignKey(User, on_delete=CASCADE, max_length=255)
    pub_date = models.DateTimeField()


class User(AbstractUser):
    USER = 'Пользователь'
    MODERATOR = 'Модератор'
    ADMIN = 'Админ'
    ROLES_CHOICES= [
        (USER,'Пользователь' ),
        (MODERATOR = 'Модератор'),
        (ADMIN = 'Админ'),
    ]
    username = models.CharField(max_length=150, unique=True, blank=False)
    username_validator = ASCIIUsernameValidator()
    email = models.EmailField(max_length=254, blank=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    bio = models.CharField()
    role = models.CharField(choices=ROLES_CHOICES, default=USER)
    password = models.CharField(blank=False)
    is_active = models.IntegerField ()