from __future__ import unicode_literals
import timezone

from django.db import models

# Create your models here.


class ATC(models.Model):
    """
    ATC代码：解剖学治疗学及化学分类系统，简称ATC(Anatomical Therapeutic
Chemical)系统，是世界卫生组织对药品的官方分类系统。
    ATC系统由世界卫生组织药物统计方法整合中心(The WHO Collaborating Centre
for Drug Statistics Methodology)所制定，第一版在1976年发布。1996年，ATC系统成为
国际标准。现在ATC系统已经发布2006版。
    ATC代码共有7位，其中第1、4、5位为字母，第2、3、6、7位为数字。 ATC系统将药物
分为5个级别
    ATC代码第一级为一位字母，表示解剖学上的分类，共有14个组别。
    ATC代码第二级为两位数字，表示治疗学上的分类。
    ATC代码第三级为一位字母，表示药理学上的分类。
    ATC代码第四级为一位字母，表示化学上的分类。
    ATC代码第五级为两位数字，表示化合物上的分类。
    """
    code = models.CharField(max_length=7, unique=True)
    name = models.CharField(_('name'), unique=True, max_length=100)
    pinyin = models.CharField(max_length=50, blank=True, null=False, default='')
    brand = models.CharField( _('brand'), max_length=50, null=False, default='',
        blank=True)
    price = models.DecimalField(_('price'), max_digits=9, decimal_places=2,
                                default=0.00)
    old_price = models.DecimalField(_('old_price'), max_digits=9,
                                    decimal_places=2, blank=True, default=0.00)
    is_active = models.BooleanField(_('is_active'), default=False)
    sold_amount = models.PositiveIntegerField(_('sold_amount'), null=False,
                                              default=10000)
    is_bestseller = models.BooleanField(_('is_bestseller'), default=False)
    end_datetime = models.DateTimeField(default=timezone.now)
    description = models.TextField(
        _('description'),
        blank=True, null=False, default='')
    meta_keywords = models.CharField(_('meta keywords'), max_length=255,
                                     help_text=_('Comma-delimited set of \
                                     SEO keywords for meta tag'), blank=True,
                                     null=False, default='')
    meta_description = models.CharField(_('meta description'), max_length=255,
                                        help_text=_('Content for description \
                                        meta tag'), blank=True, null=False, default='')
    manufacturer = models.CharField(_('manufacturer'), max_length=300,
                                    blank=True, default='')
    created_at = models.DateTimeField(_('created_at'), default=timezone.now)
    updated_at = models.DateTimeField(_('updated_at'), default=timezone.now)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.name


class NEML(models.Model):
    """
    National Essential Medicine List 《国家基本药物目录》
    """
    pass


class BNMIEML(models.Model):
    """
    Basic National Medical Insurance Essential Medicine List
    《国家基本医疗保险药品目录》已经专家论证通过，由劳动和社会保障部正式颁布。
    颁布的目录是经劳动保障部、国家计委等７个部门确定的专家小组对药品进行分类并
    拟定备选目录，由全国１０００多名专家投票遴选等严格程序产生的。《国家基本医
    疗保险药品目录》包括西药、中成药(含民族药)和中药饮片三个部分。制定基本医疗
    保险药品目录，加强基本医疗保险用药管理，是保障职工基本用药需求，合理控制医
    药费用，推进基本医疗保险改革的重要措施。
    """
    code = models.CharField(max_length=10, unique=True)

