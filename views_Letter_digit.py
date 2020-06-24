from RosenmeisterApp import Service
from RosenmeisterApp import serializers
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.core.exceptions import SuspiciousOperation
from rest_framework.exceptions import APIException,ValidationError

# This is considered as different resource, so i have created new API View class for Letter_Digit service
class Letter_digit(CreateAPIView):
    serializer_class = serializers.Letter_digitSerializer
    queryset = ""

    def create(self, request, *args, **kwargs):
        """
        This is Create an API-Endpoint taking a string with letters and digits and returning a list of all
        possible upper & lowercase variations.
        :param request:
        :param args:
        :param kwargs:
        :return: dictionary
        """
        try:
            success =  True
            values = Service.Letter_digitservice()
            val_dct=values.show_string(request.data['value'])
            ser = self.get_serializer(data = val_dct)
            if ser.is_valid():
                custom_data = {
                    request.data['value']: ser.data['value'],
                }
            else:
                raise ValidationError("Validation Error -", ser.errors)
        except SuspiciousOperation as e:
            success = False
            raise SuspiciousOperation("This is bad request, kindly check",e)
        except APIException as e:
            success = False
            raise APIException(e.get_full_details())
        else:
            if success:
                return Response(custom_data)
            else:
                return Response({"Error":"Errors present"})


