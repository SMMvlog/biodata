from app.models import Resume
from app.api.serializers import ResumeSerializer
from rest_framework import viewsets

class Homeapi(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
