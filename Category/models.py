from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=100, null=True, blank=True)
    born = models.PositiveIntegerField(null=True, blank=True)
    died = models.PositiveIntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    known_for = models.CharField(max_length=200, null=True, blank=True)
    notable_work = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField()
    year = models.PositiveIntegerField(null=True, blank=True)
    medium = models.CharField(max_length=50, null=True, blank=True)
    dimensions = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    designed_by = models.CharField(max_length=50, null=True, blank=True)
    developer = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.category.name})"