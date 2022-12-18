
def choises():
    from teach.models import Categoryes
    _ = []
    for category in Categoryes.objects.all():
        _.append((category.code, category.name))
        return _    