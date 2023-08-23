from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        db_table = 'category'


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    genere = models.CharField(max_length=100,choices=(('Action','Action'),('Comedy','Comedy'),('Drama','Drama'),('Horror','Horror'),('Romance','Romance'),('Thriller','Thriller'))) 
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'blog'
        
