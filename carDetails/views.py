from datetime import datetime
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from carDetails.models import CarDetails, PCNCode, PCNTable
from carDetails.serializers import PCNCodeSerializer, PCNTableSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from users.utils import get_tokens_for_user
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.parsers import JSONParser
import easyocr
from PIL import Image
from django.core.files.storage import default_storage
# Create your views here.

class PCNView(viewsets.ViewSet):
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    def save_pcn(self,request):
        parser_classes = [MultiPartParser, FileUploadParser]
        user = request.user
        data = request.data
        number_plate = data["number_plate"]
        car_model = data["car_model"]
        car_color = data["car_color"]
        car_location = data["car_location"]
        pcn_code = data["pcn_code"]
        reason = data["reason"]
        car_image = data.get('car_image', None)
        
        if PCNCode.objects.filter(slug=pcn_code).exists():
            pcnCode = PCNCode.objects.get(slug=pcn_code)
        car_details = CarDetails(
          number_plate = number_plate,
          car_model = car_model,
          car_color = car_color,
          car_location = car_location,
          car_image = car_image
        )
        car_details.save()
        date_of_creation = datetime.now()
        pcnTable = PCNTable(
            user=user,
            carDetails = car_details,
            pcnCode = pcnCode,
            reason = reason,
            date_of_creation = date_of_creation
        )
        pcnTable.save()
        return Response(
            data={'status': True,}, 
            status=status.HTTP_200_OK
        )

    def get_pcn_code(self,request):
        dt = PCNCode.objects.all()
        res = PCNCodeSerializer(dt, many=True).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )
    def get_pcn_summary(self,request):
        dt = PCNTable.objects.all()
        res = PCNTableSerializer(dt, many=True,context={'request': request}).data
        return Response(
            data={'status': True, 'data': res}, 
            status=status.HTTP_200_OK
        )

class ImageText(viewsets.ViewSet):
    def getImage(self,request):
        reader = easyocr.Reader(['en','fr','de'],gpu=False)
        data = request.data
        file = data["file"]
        file_name = default_storage.save('image/images/'+file.name, file)
# file extension (get the las 4 chars)
        file = default_storage.open(file_name)
        # handle file extension
        file_url = default_storage.url(file)
        result = reader.readtext(file_url,detail = 0, paragraph=False)
        print(result)
        imageMessage="";
        for x in result:
            imageMessage += ' '+x
        import re
        textToDisplay = ""
        pattern = re.compile(r"[A-Z]{2}[0-9]{2}\s+[A-Z]{3}")
        a = re.search(pattern,imageMessage)
        if a is not None:
            textToDisplay = a.group(0)
        else:
            textToDisplay = imageMessage
        return Response(data={'message': textToDisplay}, status=status.HTTP_200_OK)
