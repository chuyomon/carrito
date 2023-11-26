from rest_framework import serializers 
from aplicacionESP.models import Profile

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'