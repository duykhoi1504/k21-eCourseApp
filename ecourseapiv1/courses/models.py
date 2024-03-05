from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    pass


class Category(BaseModel):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(BaseModel):
    name = models.CharField(max_length=255)
    description= models.TextField()
    image = models.ImageField(upload_to='courses/%Y/%m/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name