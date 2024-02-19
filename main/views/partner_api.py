from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models import Partner, Product, File
from main.serializers import PartnerSerializer, ProductSerializer


class GetPartner(GenericAPIView):
    serializer_class = PartnerSerializer

    def get(self, request):
        partners = Partner.objects.all()
        serialized = self.get_serializer(partners, many=True)
        return Response(serialized.data)


class ProductByPartner(GenericAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Product.objects.filter(Q(partner_id=pk))

    def get(self, request, pk):
        products = self.get_queryset()
        serializer = self.get_serializer(products, many=True)
        serialized_data = serializer.data
        product_list = []
        for product in serialized_data:
            # print(product.id)
            try:
                product_dict = {
                        "id": 1,
                        "name": product['name'],
                        "name_uz": product['name_uz'],
                        "name_ru": product['name_ru'],
                        "price": product['price'],
                        "productivity": product['productivity'],
                        "organization": product['organization'],
                        "category": product['category'],
                        "category_uz": product['category_uz'],
                        "category_ru": product['category_ru'],
                        "description": product['description'],
                        "description_uz": product['description_uz'],
                        "description_ru": product['description_ru'],
                        "image": File.objects.get(product_id=product['id']).file.url,
                        "partner_id": product['partner_id'],
                        "category_id": product['category_id'],
                      }
                product_list.append(product_dict)
            except File.DoesNotExist:
                pass
        return Response(product_list)
