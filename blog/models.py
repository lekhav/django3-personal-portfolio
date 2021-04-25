from django.db import models

# Create your models here.
class Blog(models.Model):
    post_title = models.CharField(max_length=200)
    post_timestamp = models.DateField()
    post_description = models.TextField()

    def __str__(self):
        # ADMIN PAGE ---> to display the Title inplace of the default, Blog object (#)
        return self.post_title
