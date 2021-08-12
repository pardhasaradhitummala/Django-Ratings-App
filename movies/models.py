from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_actor = models.CharField(max_length=200)
    movie_actress = models.CharField(max_length=200)
    movie_director = models.CharField(max_length=200)
    movie_production = models.CharField(max_length=200)
    movie_release_date = models.DateField()
    movie_poster = models.ImageField(upload_to='static/images/movieposter')
    def __str__(self):
        return self.movie_name


class Rating(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    person = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.FloatField(max_length=10)
    review = models.TextField()
    def __str__(self):
        return str(self.rating)