from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models import Category
from main.serializers import CategorySerializer


class CategoryGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()  # Add the queryset attribute

    def get(self, request, pk):
        try:
            category = self.get_object()
            serializer = self.get_serializer(category)
        except Category.DoesNotExist:
            return Response({"message": "Category not found"}, status=404)
        return Response(serializer.data)


class CategoryListGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()  # Add the queryset attribute

    def get(self, request):
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)
