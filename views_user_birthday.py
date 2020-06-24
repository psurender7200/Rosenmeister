from rest_framework.viewsets import ModelViewSet
from RosenmeisterApp.models import Details
from RosenmeisterApp import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import SuspiciousOperation
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.exceptions import APIException,ValidationError

class User_birthday(ModelViewSet):

    queryset = Details.objects.all()
    serializer_class = serializers.Birthday_serializer
    http_method_names = ['get', 'post']

    @method_decorator(cache_page(60 * 5))
    def list(self, request, *args, **kwargs):
        """
        This method will show all the records and also filter the records based on daterange
        using birthday coloumn.
        :param request:
        :param args:
        :param kwargs:
        :return: response with records
        """
        try:
            qs = self.get_queryset()
            date_from = request.query_params.get('date_from',None)
            date_to = request.query_params.get('date_to',None)
            print(date_from,date_to)
            if date_from is not None and date_to is not None:
                data = qs.filter(birthday__range=(date_from, date_to))
            else:
                data = qs
            ser = self.get_serializer(data,many=True)
        except APIException as e:
            raise APIException(e.get_full_details())
        else:
            return Response(ser.data)

    @action(name="avgage", detail=True, methods=['get'],url_path="Info")
    @method_decorator(cache_page(60 * 5))
    def avgage(self, request, *args, **kwargs):
        """
        This method is also get, this is used to get the average age
        :param request:
        :param args:
        :param kwargs:
        :return: return average age
        """
        try:
            self.serializer_class = serializers.Age_serializer
            qs = Details.objects.all()
            ser = self.get_serializer(qs)
        except APIException as e:
            raise APIException(e.get_full_details())
        else:
            return Response(ser.data)

    def create(self, request, *args, **kwargs):
        """
        This will create the new records in the database
        :param request:
        :param args:
        :param kwargs:
        :return: dictionary with message
        """
        try:
            success =True
            ser = self.get_serializer(data = request.data,many=True)
            print(request.data)
            if ser.is_valid():
                ser.save()
            else:
                raise ValidationError("validations Errors")
        except SuspiciousOperation as e:
            success = False
            raise SuspiciousOperation("This is bad request, kindly check",e)
        except APIException as e:
            success = False
            raise APIException(e.get_full_details())
        else:
            if success:
                return Response({"Success":"Records are created Successfully"})
            else:
                return Response({"Exception": "Errors are present"},status=500)