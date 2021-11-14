from django.contrib import admin
from .models import Publication, \
    PublicationW, PublicationI, Comments, CommentsW

# Register your models here.


admin.site.register(Publication)
admin.site.register(PublicationW)
admin.site.register(PublicationI)
admin.site.register(Comments)
admin.site.register(CommentsW)

