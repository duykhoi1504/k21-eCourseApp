from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class ItemBase(BaseModel):
    tags=models.ManyToManyField(Tag)

    class Meta:
        abstract=True


class Course(ItemBase):
    name = models.CharField(max_length=255)
    description=RichTextField()
    image = models.ImageField(upload_to='courses/%Y/%m/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lesson (ItemBase):
    subject=models.CharField(max_length=255)
    content=RichTextField()
    image= models.ImageField(upload_to='lesson/%Y/%m/')
    course=models.ForeignKey(Course,on_delete=models.CASCADE)


class Interaction(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)

    class Meta:
        abstract=True


class Comment(Interaction):
    content= models.CharField(max_length=255)


class Like(Interaction):

    class Meta:
        unique_together = ('user','lesson')
