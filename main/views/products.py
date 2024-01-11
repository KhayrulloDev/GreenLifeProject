from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models import Product, File
from main.serializers import ProductSerializer, ContactSerializer, ProductWithCategory


class ProductWithCategoryGenericAPIView(GenericAPIView):
    serializer_class = ProductWithCategory

    def get(self, request, category_id):
        try:
            products = Product.objects.filter(category_id=category_id)
            serializer = self.get_serializer(products, many=True)
            list_data = []
            for product in serializer.data:
                try:
                    product['image'] = File.objects.get(product_id=product['id']).file.url
                except File.DoesNotExist:
                    product['image'] = None
                list_data.append(product)
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(list_data)


class ProductGenericAPIView(GenericAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        # print(Product.objects.get(Q(pk=pk)))
        return Product.objects.filter(pk=pk)

    def get(self, request, pk):
        try:
            product = self.get_queryset().first()
            if not product:
                raise Product.DoesNotExist

            serializer = self.get_serializer(product)
            serialized_data = serializer.data

            product_id = serialized_data['id']
            files = File.objects.filter(product_id=product_id)
            if files.exists():
                image = files.first().file.url
                serialized_data['image'] = 'http://206.189.150.181' + image
            else:
                serialized_data['image'] = None

            return Response(serialized_data)
        except Product.DoesNotExist:
            return Response({"message": "Product not found!"}, status=404)
        except Exception as e:
            return Response({"message": str(e)}, status=500)


class ContactGenericAPIView(GenericAPIView):
    serializer_class = ContactSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(serializer.data)
