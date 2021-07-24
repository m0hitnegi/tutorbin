from django.db import models

class Image(models.Model):
    name= models.CharField(max_length=500)
    image= models.ImageField(upload_to='', null=True, verbose_name="")

    def __str__(self):
        return str(self.image)


class Tags(models.Model):
    tag = models.CharField(max_length=50)
    img = models.ManyToManyField(Image)


    def __str__(self):
        return self.tag