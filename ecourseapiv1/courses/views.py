from rest_framework import viewsets, generics,status,parsers,permissions
from courses import serializers, paginators
from courses.models import Category, Course,Lesson,User
from rest_framework.decorators import action
from rest_framework.response import Response



class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = serializers.CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePaginator

    def get_queryset(self):
        queryset = self.queryset

        if self.action.__eq__('list'):
            q = self.request.query_params.get('q')
            if q:
                queryset = queryset.filter(name__icontains=q)

            cate_id = self.request.query_params.get('category_id')
            if cate_id:
                #nếu dùng category__id nó sẽ thực hiện join bảng Category đề lấy ID
                #ở đây ta đã có category_id( tên nó tự sinh ra)
                # -> dùng sẽ đỡ tốn truy vấn
                #-> tốc dộ nhanh hơn
                queryset = queryset.filter(category_id=cate_id)

        return queryset

    @action(methods=['get'],url_path='lessons',detail=True)
        #detail True mới có chi tiết {course_id}
        #detail = True mới có pk nếu false - > bỏ pk
    def get_lessons(self,request,pk):
        lessons=self.get_object().lesson_set.filter(active=True)

        q=request.query_params.get('q')
        if q:
            lessons=lessons.filter(subject__icontains=q)

        return Response(serializers.LessonSerializer(lessons,many=True).data,
                        status=status.HTTP_200_OK)


class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    # prefetch_related('tags') lấy sẵn cái tag
    queryset = Lesson.objects.prefetch_related('tags').filter(active=True)
    serializer_class =  serializers.LessonDetailsSerializer

    @action(methods=['get'],url_path='comments',detail=True)
    def get_comments(self,request,pk):
        #
        # queryset = self.filter_queryset(self.get_queryset())
        #
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = serializers.CommentSerializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        # serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)
        #
        comments=self.get_object().comment_set.order_by('-id')

        paginator=paginators.CommentPaginator()
        page = paginator.paginate_queryset(comments,request)
        if page is not None:
            serializer = serializers.CommentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        return Response(serializers.CommentSerializer(comments,many=True).data)


class UserViewSet(viewsets.ViewSet,generics.CreateAPIView):
    queryset=User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser,]

    def get_permissions(self):
        if self.action in['get_current_user']:
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get','patch'],url_path='current-user',detail=False)
    def get_current_user(self,request):

        user=request.user
        if request.method.__eq__('PATCH'):
            for k, v in request.data.items():
                setattr(user,k,v)
            user.save()

        return Response(serializers.UserSerializer(user).data)