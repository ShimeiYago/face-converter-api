# -*- encoding: utf-8 -*-

# from rest_framework.permissions import IsAuthenticated
# from django.core.mail import send_mail
from rest_framework.generics import GenericAPIView
from django.conf import settings
from utils.tf import convert_image
from convert.serializers import ConvertSerializer
from rest_framework.response import Response
from rest_framework import status

# from drf_yasg.utils import swagger_auto_schema


class ConvertView(GenericAPIView):
    serializer_class = ConvertSerializer

    def post(self, request, *args, **kwargs):
        [wholeImgBase64data, croppedImgBase64data] = convert_image(
            request.data["base64data"],
            request.data["convertDirection"],
            request.data["crop"],
        )

        res = {
            "wholeImgBase64data": wholeImgBase64data,
            "croppedImgBase64data": croppedImgBase64data
        }
        return Response(status=status.HTTP_200_OK, data=res)
