from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)


    def __str__(self):
        # to display the Title inplace of default Blog object (#) in ADMIN PAGE
        return self.title            
    

# class Home(models.Model):
#     print('Welcome to my Portfolio. I have listed my Projects, Experiences,...')
