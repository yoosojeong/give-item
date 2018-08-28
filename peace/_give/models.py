from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# ------------------------------------------------------------------
# TableName   : ItemPostModel
# Description : 중고 아이템 올리는 테이블
# ------------------------------------------------------------------
class ItemPostModel(TimeStampedModel):
    class Meta:
        verbose_name_plural = "중고 아이템 올리는 테이블"

    TYPE_CHOICES = (
        ('여성의류', '여성의류'),
        ('남성의류', '남성의류'),
        ('뷰피/미용', '뷰피/미용'),
        ('유아동/출산', '유아동/출산'),
        ('스포츠/레저', '스포츠/레저'),
        ('디지털/가전', '디지털/가전'),
        ('도서/티켓/취미/애완', '도서/티켓/취미/애완'),
        ('생활/문구/가구/식품', '생활/문구/가구/식품'),
        ('차량/오토바이', '차량/오토바이'),
        ('스타굿즈', '스타굿즈'),
        ('기타', '기타'),
        ('평화나눔', '평화나눔'),
    )

    STATE_CHOICES = (
        ('중고', '중고'),
        ('중고 + 하자 (하자가 없는 중고)', '중고 + 하자 (하자가 없는 중고)'),
        ('새것 + 하자 (하자가 없는 새것)', '새것 + 하자 (하자가 없는 새것)'),
        ('거의 새것 (하자 없음)', '거의 새것 (하자 없음)'),
        ('새물품 (미사용)', '새물품 (미사용)'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='유저')
    images = models.ImageField(null=True, blank=True)
    type_item = models.CharField(max_length=32, choices=TYPE_CHOICES ,  verbose_name='카테고리')
    state_item = models.CharField(max_length=32, choices=STATE_CHOICES , verbose_name='상태')
    location = models.CharField(max_length=32, verbose_name='거래지역')
    title = models.CharField(max_length=64, verbose_name='제품명')
    cost = models.PositiveIntegerField(verbose_name='예상금액')
    contents = models.TextField(verbose_name='내용')
    amount = models.PositiveIntegerField(verbose_name='갯수')
    tags = TaggableManager()


    def __str__(self):
        return '상품명: {} / 판매자: {}'.format(self.title, self.user)
        
# ------------------------------------------------------------------
# TableName   : ItemPickModel
# Description : 내가 찜한 중고 아이템 테이블
# ------------------------------------------------------------------
class ItemPickModel(models.Model):
    class Meta:
        verbose_name_plural = "내가 찜한 중고 아이템 테이블"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='유저')
    item = models.ForeignKey(ItemPostModel, on_delete=models.CASCADE, verbose_name='프로젝트')
