from django.db import models

# Create your models here.


class Datavisualization(models.Model):
    end_year=models.IntegerField(null=True)
    intensity=models.IntegerField(null=True)
    sector=models.CharField(max_length=100,null=True)
    topic=models.CharField(max_length=100,null=True)
    url=models.CharField(max_length=100,null=True)
    region=models.CharField(max_length=100,null=True)
    start_year=models.CharField(max_length=100,null=True)
    impact=models.CharField(max_length=100,null=True)
    added=models.CharField(max_length=100,null=True)
    published=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    relevance=models.IntegerField(null=True)
    pestle=models.CharField(max_length=100,null=True)
    source=models.CharField(max_length=100,null=True)
    title=models.CharField(max_length=100,null=True)
    likelihood=models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.intensity)

