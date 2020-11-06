from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    thumbnail_size = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ("id", "file", "thumbnail", "thumbnail_size", "width", "height", "size", "extension")
        extra_kwargs = {
            "id": {"read_only": True},
            "width": {"read_only": True},
            "height": {"read_only": True},
            "size": {"read_only": True},
            "extension": {"read_only": True},
        }

    def get_thumbnail(self, img: Image):
        return self.context.get("request").build_absolute_uri(img.file.thumbnail.url)

    def get_thumbnail_size(self, img: Image):
        return {k: v for k, v in img.file.field.variations.get("thumbnail").items() if k in ("width", "height")}


class CreateImageSerializer(serializers.ModelSerializer):
    files = serializers.ListField(child=serializers.ImageField(), required=True)

    class Meta:
        model = Image
        fields = ("files",)
