from django.db import models

class News(models.Model):
    heading=models.CharField(max_length=20)
    description=models.TextField()
    creation_date=models.DateField()
    update_date=models.DateField()