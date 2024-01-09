from rest_framework.serializers import ModelSerializer
from .models import Partner, Product, Contact, Category, Blog
from .models.about import About


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name_en', 'name_uz', 'name_ru')


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductWithCategory(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name_en', 'name_uz', 'name_ru', 'productivity')


class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class BlogSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'title_en', 'title_uz', 'title_ru', 'image')


class BlogDetailSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class AboutSerializer(ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'
