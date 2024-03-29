from django.db import models


class EBooksModel(models.Model):
 
    title = models.CharField(max_length = 80)
    pdf = models.FileField(upload_to='pdfs/')
 
    class Meta:
        ordering = ['title']
     
    def __str__(self):
        return f"{self.title}"

# Create your models here.
