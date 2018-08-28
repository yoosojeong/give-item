from django.contrib import admin
from .models import *

# ------------------------------------------------------------------
# TableName   : ItemPostModel
# Description : 중고 아이템 올리는 테이블
# ------------------------------------------------------------------
@admin.register(ItemPostModel)
class ItemPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'type_item', 'state_item', 'location', 'title', 'cost', 'contents', 'amount', 'tag_list']

    def get_queryset(self, request):
        return super(ItemPostAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

# ----------------------1--------------------------------------------
# TableName   : ItemPickModel
# Description : 내가 찜한 중고 아이템 테이블
# ------------------------------------------------------------------
@admin.register(ItemPickModel)
class ItemPickAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'item']