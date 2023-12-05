# # from django.contrib import admin
# # from .models import Article
# # from django.utils.safestring import mark_safe
# # from django.utils.html import format_html


# # @admin.register(Article)
# # class ArticleAdmin(admin.ModelAdmin):
# #     list_display = ('display_image','title','author','description', 'get_content_html', 'published_date')
    
# #     list_filter = ('title', 'author', 'published_date')
# #     search_fields = ('title', 'author', 'published_date')
# #     # list_editable = ('title', 'author',)
# #     list_display_links = ('title',)
    
# #     def get_content_html(self, obj):
# #         return mark_safe(obj.content)
# #     get_content_html.short_description = 'Content'  # Optional: Set a header for the column
    
# #     def display_image(self, obj):
# #         return format_html('<img src="{}" width="60" height="60" />', obj.image.url)
# #     display_image.short_description = "L'image"
# #     # display_image.short_description = trans("L'image de l'etudiant ")



# # # admin.site.register(Article)

# # admin.site.site_title = "Minister de l'exterieure"  # This will change the title tag
# # admin.site.site_header = "Minister de l'exterieure"  # This will change the header text


# # admin.py

# # admin.py

# # admin.py
# from django.contrib import admin
# from .models import Article, Test as YourModel
# from firebase_admin import firestore



# def sync_data_with_firestore(YourModel, request, queryset):
#     for obj in queryset:
#         # Example: Add data to Firestore
#         collection_ref = firestore.client().collection('your_collection_name')
#         doc_ref = collection_ref.add({
#             'name': obj.name,
#             'description': obj.description,
#         })

#         # Store the Firestore document ID in your Django model
#         # obj.firestore_document_id = doc_ref.id
#         obj.save()

# sync_data_with_firestore.short_description = "Sync selected items with Firestore"

# class YourModelAdmin(admin.ModelAdmin):
#     actions = [sync_data_with_firestore]
#     list_display = ['name', 'description', 'firestore_document_id']

# admin.site.register(YourModel, YourModelAdmin)
# admin.site.register(Article)
