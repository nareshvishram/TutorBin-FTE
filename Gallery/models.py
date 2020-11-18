from django.db import models


# Create your models here.
class Image_Tags(models.Model):
    tags=models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        if self.tags:
              return self.tags
        return 'No Tag'

class Image(models.Model):
    title=models.TextField(max_length=20,null=True,blank=True)
    tags=models.ForeignKey(Image_Tags,on_delete=models.SET_NULL,null=True,blank=True)
   # tags=models.CharField(max_length=20,null=True,blank=True)
    image=models.ImageField(null=True,upload_to='Upload/',blank=True)
    description=models.TextField(max_length=100,null=True,blank=True)

    def __str__(self):
        if self.tags:
            return str(self.tags)
        return 'No Image'

