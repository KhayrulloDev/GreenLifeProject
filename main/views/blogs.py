from main.models.blogs import Blog
from rest_framework.generics import GenericAPIView
from main.serializers import BlogSerializer, BlogDetailSerializer
from rest_framework.response import Response


class BlogListGenericAPIView(GenericAPIView):
    serializer_class = BlogSerializer

    def get(self, request):
        try:
            blogs = Blog.objects.all().order_by('-id')
            serializer = self.get_serializer(blogs, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"message": str(e)}, status=500)


class BlogDetailGenericAPIView(GenericAPIView):
    serializer_class = BlogDetailSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Blog.objects.filter(pk=pk)

    def get(self, request, pk):
        try:
            blog = self.get_queryset().first()
            if not blog:
                raise Blog.DoesNotExist

            serializer = self.get_serializer(blog)
            return Response(serializer.data)
        except Blog.DoesNotExist:
            return Response({"message": "Blog not found!"}, status=404)
        except Exception as e:
            return Response({"message": str(e)}, status=500)

