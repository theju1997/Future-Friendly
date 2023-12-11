from django.db import models


# Create your models here.
class CustomerData(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    ratings=models.IntegerField()
    feedback=models.TextField()

class Catagory(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    description=models.TextField(max_length=150,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hodden")
    created_at=models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.name    

    
   