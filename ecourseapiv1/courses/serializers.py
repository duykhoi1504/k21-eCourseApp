from rest_framework import serializers
from courses.models import Category, Course, Lesson,Tag,User,Comment

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


class UserSerializer(serializers.ModelSerializer):

    def create (seft,validated_data):
        data=validated_data.copy()

        user=User(**data)
        user.set_password(data["password"])
        user.save()

        return user


    class Meta:
        model=User
        fields=['id','first_name','last_name','email','username','password','avatar']

        # giúp password ko bị trả vè
        extra_kwargs={
            'password':{
                'write_only':True
            }
        }

class CommentSerializer(serializers.ModelSerializer):
    user=UserSerializer()

    class Meta:
        model=Comment
        fields=['id','content','created_date','user']
