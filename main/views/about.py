from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from main.models.about import About
from main.serializers import AboutSerializer


class AboutGenericAPIView(GenericAPIView):
    serializer_class = AboutSerializer

    def get(self, request):
        text = About.objects.all().first()
        serializer = self.get_serializer(text)
        return Response(serializer.data)
