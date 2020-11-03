from django.db import models


class Work(models.Model):
    '''
    The Work model class that represents the portfolio's artworks.
    Contains five descriptive fields about the artwork.
    '''
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    description = models.TextField()
    medium = models.CharField(max_length=50)
    image = models.FilePathField(path='/img')
