from django.urls import path
from .views import GetPartner, ProductByPartner
from .views.blogs import BlogListGenericAPIView, BlogDetailGenericAPIView
from .views.categories import CategoryGenericAPIView, CategoryListGenericAPIView
from .views.products import ProductWithCategoryGenericAPIView, ContactGenericAPIView, ProductGenericAPIView


urlpatterns = [
    path('category-list', CategoryListGenericAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryGenericAPIView.as_view(), name='categories'),
    path('product-detail/<int:pk>', ProductGenericAPIView.as_view(), name='product_detail'),
    path('products/<int:category_id>', ProductWithCategoryGenericAPIView.as_view(), name='products'),
    path('contact', ContactGenericAPIView.as_view(), name='contact'),
    path('blog-list', BlogListGenericAPIView.as_view(), name='blog_list'),
    path('blog-detail<int:pk>', BlogDetailGenericAPIView.as_view(), name='blog_detail'),
    path('get-partners', GetPartner.as_view(), name='partners'),
    path('partnerproduct<int:pk>', ProductByPartner.as_view(), name='partner-products'),
]
