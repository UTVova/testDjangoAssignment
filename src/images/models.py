from django.db import models
from django.utils.translation import gettext_lazy as _
from stdimage import StdImageField


class Image(models.Model):
    file = StdImageField(
        _("File of the image"),
        upload_to="images/%Y/%m/%d/",
        height_field="height",
        width_field="width",
        variations={"thumbnail": (100, 100)},
    )
    width = models.PositiveIntegerField(_("Width of image"))
    height = models.PositiveIntegerField(_("Height of image"))
    size = models.PositiveIntegerField(_("Size of the image file"))
    extension = models.CharField(_("Extension of the image file"), max_length=8)
