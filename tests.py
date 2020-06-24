import os
import django
import unittest
from faker import Faker
from django.test import TestCase
from rest_framework import status
from Rosenmeister.wsgi import application
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.core.wsgi import get_wsgi_application
from RosenmeisterApp.models import Details,LettersDigits
from rest_framework.exceptions import APIException,ValidationError
from RosenmeisterApp.tests_Config import EXISTING_JSON_DATA,NEW_JSON_DATA,LETTERS_DIGITS_DATA,DATE_FROM,DATE_TO

class Testing(APITestCase):

    def setUp(self) :
        """
        This is for setup process to start unit testing
        :return: None
        """
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Rosenmeister.settings")
        application = get_wsgi_application()
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        self.faker = Faker("en_IN")
        django.setup()


    def test_birthday_get_api(self):
        """
        This method by default get all the records from database and also, the same endpoint url is used for post
        which is present in next test method.
        :return: return 200
        """
        print("====================test_birthday_get_api===========================================================")
        client = APIClient()
        response = client.get('/birthday/')
        print(response.data)
        #uncomment below line and make sure to keep the length, based on the count of entries present in database, then you can test to see count od records.
        #assert len(response.data) ==4
        assert response.status_code ==200

    def test_create_api_newData(self):
        """
        This method will create the new records in the database and mailid should be unique to create
        new records in database.
        always data should be unique for creating new entries.
        :return: 200 response
        """
        print("====================test_create_api_newData======================================================")
        data = NEW_JSON_DATA
        response = self.client.post("/birthday/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Details.objects.count()::::",Details.objects.count())
        self.assertEqual(Details.objects.count(), 4)
        assert str(response.data['Success'] == "Records are created Successfully")



    def test_get_api_filter_birthday(self):
        """
        This method is to filter the data based on the birthday date, from_date - to date.
        SO please provide the dates to the URL, so that automatically you can see the filtered data.

        before you are executing this method,please make sure data is present in database with the date range used, otherwise it fetch empty
        :return: 200 response
        """
        print("====================test_get_api_filter_birthday======================================================")
        client = APIClient()
        data = NEW_JSON_DATA
        response = self.client.post("/birthday/", data, format='json')
        response = client.get("/birthday/?date_from="+ DATE_FROM +"&"+"date_to="+ DATE_TO)
        print(response.data)
        self.assertEqual(Details.objects.count(), 4)
        assert response.status_code ==200


    def test_getAPI_average_age(self):
        """
        This method is used to get the average age in years.
        before executing this method, make sure to execute create API for creating records.
        :return: 200 response
        """
        print("====================test_getAPI_average_age======================================================")
        client = APIClient()
        response = client.get('/birthday/avgage/Info/')
        print(response.data)
        self.assertIsInstance(response.data['average_age'],float)
        assert dict(response.data)
        assert response.status_code ==200


    def test_create_api_existingData(self):
        """birthday/avgage/Info/
        This method is check validations, if you try to insert data which is already existing in database. if you try to insert the data,
        then it should give validation error as this data is already present, Before checking this testcase, you need to make sure, the same
        data is already present in database --> first create the same data in database, then you can test this functionality
        :return: 500 response
        """
        print("====================test_create_api_existingData======================================================")
        client = APIClient()
        response = client.post('/birthday/',EXISTING_JSON_DATA , format='json')
        print(type(response.data))
        self.assertRaises(ValidationError)
        assert response.status_code ==500


    def test_creatapi_letters_nums(self):
        """This method is used to take a string with letters and digits and returning a list of all
        possible upper & lowercase variations.
        :return: 200 response
            """
        print("====================test_creatapi_letters_nums======================================================")
        client = APIClient()
        response = client.post('/letterdigit/', LETTERS_DIGITS_DATA, format='json')
        print(response.data)
        self.assertDictEqual(response.data,{'a2b': ['A2B', 'A2b', 'a2B', 'a2b']})
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()

