from rest_framework import serializers, viewsets
from .models import Room


class RoomSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Room
        fields = ('title', 'description')

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def get_queryset(self):
        return Room.objects.all()