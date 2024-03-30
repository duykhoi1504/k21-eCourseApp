from rest_framework import serializers
from courses.models import Category, Course, Lesson,Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields= '__all__'


class ItemSerializer(serializers.ModelSerializer):
    # để hiễn thị dường dẫn tuyệt đối của ảnh trên swagger
    # -> dễ dàng bảo trì
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = instance.image.url

        return rep



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields= ['id','name']


class CourseSerializer(ItemSerializer):

    class Meta:
        model=Course
        fields=['id','name','image','created_date','updated_date','category']


class LessonSerializer(ItemSerializer):
    class Meta:
        model=Lesson
        #do nó lấy thông tin vaắng tắt nên ko trả ra
        fields=['id','subject','image','created_date','updated_date']


class LessonDetailsSerializer(LessonSerializer):
    tags=TagSerializer(many=True)

    class Meta:
        model=LessonSerializer.Meta.model
        fields=LessonSerializer.Meta.fields + ['content','tags']