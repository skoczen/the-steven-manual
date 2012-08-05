from django.contrib import admin
from main_site.models import Emotion, EmotionEvent, Value
    

# class ArtworkOptions(admin.ModelAdmin):
#     list_display = ('name','date_added','order',)
#     search_fields = ('name','description',)
#     exclude = ("slug",)
  
#     class Media:
#         js = (
#             'js/jquery.js',
#             'js/jquery-ui.js',
#             'js/admin-list-reorder.js',
#         )

#     list_editable = ['order']  # 'order' is the name of the model field which holds the position of an element
    

# admin.site.register(Artwork,ArtworkOptions)
admin.site.register(Emotion)
admin.site.register(EmotionEvent)
admin.site.register(Value)