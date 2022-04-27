from django.contrib import admin
from django.urls import path

from carDetails.views import ImageText, PCNView

urlpatterns = [
    path('pcn/save/', PCNView.as_view({'post': 'save_pcn'})),
    path('pcn/code/', PCNView.as_view({'get': 'get_pcn_code'})),
    path('pcn/summary/',PCNView.as_view({'get': 'get_pcn_summary'})),
    path('pcn/image/',ImageText.as_view({'post':'getImage'})),
]
