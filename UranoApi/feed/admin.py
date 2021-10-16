from django.contrib import admin
from .models import Publication, \
    PublicationW, PublicationI

# Register your models here.


admin.site.register(Publication)
admin.site.register(PublicationW)
admin.site.register(PublicationI)
