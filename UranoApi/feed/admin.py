from django.contrib import admin
from .models import Publication, \
    PublicationW, PublicationI, \
    ImgPublication, VideoPublication, \
    PdfPublication


# Register your models here.
class ImagePublicationsInline(admin.TabularInline):
    model = ImgPublication
    extra = 1
    max_num = 2


class VideoPublicationInline(admin.TabularInline):
    model = VideoPublication
    extra = 1
    max_num = 1


class FilePublicationInline(admin.TabularInline):
    model = PdfPublication
    extra = 1
    max_num = 1


class PublicationAdmin(admin.ModelAdmin):
    inlines = [ImagePublicationsInline, VideoPublicationInline, FilePublicationInline]


admin.site.register(Publication, PublicationAdmin)
admin.site.register(PublicationW)
admin.site.register(PublicationI)
