from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models import Category
from main.serializers import CategorySerializer


class CategoryGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request, pk):
        try:
            categories = Category.objects.filter(pk=pk).first()
            serializer = self.get_serializer(categories, many=True)
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(serializer.data)


class CategoryListGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = self.get_serializer(categories, many=True)
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(serializer.data)
