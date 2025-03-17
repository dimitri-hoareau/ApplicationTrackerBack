from rest_framework import viewsets
from covergenerator.models import Application
from covergenerator.serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
