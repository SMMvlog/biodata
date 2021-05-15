from rest_framework import serializers
from app.models import Resume
class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resume
        # fields = ['id','url','name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','myfile']
        fields = "__all__"