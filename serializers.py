from rest_framework import serializers
from RosenmeisterApp.models import Details,LettersDigits
from django_filters.filters import DateRangeFilter
from django.db.models import Avg,F

class Age_serializer(serializers.ModelSerializer):
    average_age = serializers.SerializerMethodField()
    class Meta:
        model = Details
        fields = ['average_age',]

    def get_average_age(self, instance):
        """
        This method will give the average age of all the data
        :param instance:
        :return: return average age.
        """
        print(instance)
        everything_avg = Details.objects.all().aggregate(avg_age=Avg(F('created') - F('birthday')))
        avgage = everything_avg['avg_age'].days / 365
        return avgage

class Birthday_serializer(serializers.ModelSerializer):
    """
        This is the serializer for the Birthday service
    """
    birthday=serializers.DateField(input_formats=['%d.%m.%Y'])
    date_range = DateRangeFilter(field_name='birthday')
    class Meta:
        model = Details
        fields = ['first_name',"last_name","email","birthday"]

class Letter_digitSerializer(serializers.ModelSerializer):
    """
    This is the serializer for the Letter_digit service
    """
    value = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = LettersDigits
        fields = ['value']