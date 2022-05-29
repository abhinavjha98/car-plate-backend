from datetime import datetime
from carDetails.models import CarDetails, PCNCode, PCNTable
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PCNCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCNCode
        fields = '__all__'

class PCNTableSerializer(serializers.ModelSerializer):
    carDetails = serializers.SerializerMethodField()
    pcnCode = serializers.SerializerMethodField()
    dateOfCreation = serializers.SerializerMethodField()

    def get_carDetails(self,obj):
        
            cardetails = CarDetails.objects.filter(id=obj.id)
            print(cardetails)
            data = [{"number_plate": i.number_plate,"car_model":i.car_model,"car_color":i.car_color,"car_location":i.car_location,"car_image":self.context['request'].build_absolute_uri(i.car_image.url)if i.car_image else None} for i in cardetails]
            return data
        
            

    def get_pcnCode(self,obj):
        try:
            print(obj.id)
            pcnTable = PCNTable.objects.get(id=obj.id)
            print(pcnTable.pcnCode.slug)
            pcnCode = PCNCode.objects.filter(slug=pcnTable.pcnCode.slug)
            data = [{"pcnCode": i.pcnCode,"slug":i.slug} for i in pcnCode]
            return data
        except:
            return None

    def get_dateOfCreation(self,obj):
        date_format = "%Y-%m-%d %H:%M:%S %p"
        return datetime.strftime(obj.date_of_creation,date_format)

    class Meta:
        model = PCNTable
        exclude = ('created_at', 'updated_at','date_of_creation','user')
        
