from rest_framework import viewsets
from aplicacionESP.models import Profile
from aplicacionESP.serializers import MemberSerializer

class MembersViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = MemberSerializer