import os
import tempfile

from django.conf import settings


def temp_file():
    tmp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
    with open(tmp_file.name, "wb") as file_write, open(
        os.path.join(settings.BASE_DIR, "images", "tests", "resources", "img.png"), "rb"
    ) as file_read:
        file_write.write(file_read.read())
    return tmp_file
