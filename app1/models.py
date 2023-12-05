# from django.db import models
# # from tinymce.models import HTMLField
# from django.utils.translation import gettext_lazy as _
# from django.utils.safestring import mark_safe

# class Article(models.Model):
#     # image = models.FileField(_("Image"), upload_to='uploads/', default=None)
#     title = models.CharField(_("Title"),max_length=200)
#     author = models.CharField(_("Author"),max_length=100)
#     content = models.TextField()
#     # content = HTMLField(_("Content"),)
#     published_date = models.DateTimeField(_("Published date"),auto_now_add=True)
    
#     def get_content_html(self):
#         return mark_safe(self.content)
    
    
#     class Meta:
#         verbose_name = _("Article")
#         verbose_name_plural = _("Articles")

#     def __str__(self):
#         return self.title
    
    
# class Test(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     firestore_document_id = models.CharField(max_length=255, blank=True, null=True)

#     def to_dict(self):
#         return {
#             'name': self.name,
#             'description': self.description,
#             'firestore_document_id': self.firestore_document_id
#         }
 

