import os
from typing import List

from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer
from rest_framework.viewsets import GenericViewSet

from .models import Image
from .serializers import CreateImageSerializer, ImageSerializer


class ImageViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet
):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateImageSerializer
        return self.serializer_class

    def perform_create(self, serializer) -> List[BaseSerializer]:
        """Pass files from ListField to separate serializers, validate and save them."""
        files = serializer.validated_data.get("files")
        image_serializer = self.serializer_class
        serializers = [image_serializer(data={"file": file}, context=self.get_serializer_context()) for file in files]
        for serializer in serializers:
            serializer.is_valid(True)

        for serializer in serializers:
            serializer.save(
                size=serializer.validated_data.get("file").size,
                extension=os.path.splitext(serializer.validated_data.get("file").name)[1][1:],
            )
        return serializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_serializers = self.perform_create(serializer)
        return Response({"files": [s.data for s in image_serializers]}, status=status.HTTP_201_CREATED)
