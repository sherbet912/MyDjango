from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from markdownx.models import MarkdownxField
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User

# Create your models here.
def material_image_upload_to(instance, filename):
    kind = instance.kind or 'others'
    return f"material_images/{kind}/{filename}"

    
class MaterialImage(models.Model):
    KIND_CHOICES = [
        ("icon", "Icon"),
        ("cover", "Cover"),
        ("screenshot", "Screenshot"),
    ]
    name = models.CharField("名稱", max_length=255)
    kind = models.CharField("類型", max_length=20, choices=KIND_CHOICES)
    image = models.ImageField("圖片", upload_to=material_image_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Article(models.Model):
    title = models.CharField("標題", max_length=255)
    cover = models.ForeignKey(MaterialImage, on_delete=models.SET_NULL, null=True, verbose_name="封面圖")
    content = RichTextUploadingField("html內容")
    content2 = MarkdownxField("md內容", null=True)
    content3 = MDTextField("md2內容", null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_at = models.DateTimeField("建立時間", auto_now_add=True)
    updated_at = models.DateTimeField("更新時間", auto_now=True)
    
    def __str__(self):
        return self.title