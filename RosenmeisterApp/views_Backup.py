from rest_framework.generics import ListCreateAPIView
from RosenmeisterApp.models import Details
from RosenmeisterApp import serializers
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

# Create your views here.

class user_birthday(ListCreateAPIView):
    queryset = Details.objects.all()
    serializer_class = serializers.Birthday_serializer

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        start = request.query_params.get('start')
        end = request.query_params.get('end')
        data = qs.filter(birthday__range=(start, end))
        ser = self.get_serializer(data,many=True)
        print(ser.data)
        return Response(ser.data)

    def create(self, request, *args, **kwargs):

        print(request.data)
        ser = self.get_serializer(data = request.data,many=True)
        if ser.is_valid():
            ser.save()
        else:
            print("========================================")
            raise ValidationError(ser.errors)
            #print(ser.errors)
        return Response({"Created":"Yes Created"})


