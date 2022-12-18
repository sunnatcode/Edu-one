
from uuid import uuid4


def media_path(file_name):
    return f'media/uploads/{file_name}'

def store_file(file):
    from ..models import Uploads
    code = uuid4
    new_name = file.name + uuid4

    uploads = Uploads(
        original_name = file.name,
        content_type = file.content_type,
        size = file.size,
        code = code,
        new_name = new_name,
        path = media_path(file.name)

    )

def choises():
    from teach.models import Categoryes
    _ = []
    for category in Categoryes.objects.all():
        _.append((category.code, category.name))
        return _    