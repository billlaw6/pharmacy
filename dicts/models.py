from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from django.core.validators import RegexValidator

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
    atc_validator = RegexValidator(regex='^[a-z][0-9]*2[a-z]*2[0-9]*2')
    atc_code = models.CharField(max_length=7, unique=True,
                                null=True, blank=True,
                                validators=[atc_validator])
    anatomia_code = models.CharField(max_length=1, null=True, blank=True,
                                     help_text='解剖学上的分类')
    therapeutics_code = models.CharField(max_length=2, null=True, blank=True,
                                         help_text='治疗学上的分类')
    pharmacology_code = models.CharField(max_length=1, null=True, blank=True,
                                         help_text='药理学上的分类')
    chemical_code = models.CharField(max_length=1, null=True, blank=True,
                                     help_text='化学上的分类')
    compound_code = models.CharField(max_length=2, null=True, blank=True,
                                     help_text='化合物上的分类')

    class Meta:
        ordering = ('atc_code',)
        verbose_name = '药品ATC编码'

    def __str__(self):
        return self.atc_code


class DrugName(models.Model):
    """
    常见的西药名称有三种：通用名、英文名、商品名。
    """
    # 通用名：中国药品通用名称 China Approved Drug Names, CADN
    # 由药典委员会按照《药品通用名称命名原则》组织制定并报卫生部备案的药品的
    # 法定名称，是同一种成分或相同配方组成的药品在中国境内的通用名称，具有强
    # 制性和约束性。因此，凡上市流通的药品的标签、说明书或包装上必须要用通用
    # 名称。其命名应当符合《药品通用名称命名原则》的规定，不可用作商标注册。
    cadn_name = models.CharField(max_length=100)
    cadn_name_zh_hans = models.CharField(max_length=100)
    cadn_name_pinyin = models.CharField(
        max_length=200, blank=True, null=False, default='')
    cadn_name_py = models.CharField(
        max_length=200, blank=True, null=False, default='')
    # 英文名称采用世界卫生组织编订的国际非专利药名（International Nonproprietary
    # Names for Pharmaceutical
    # Substances，简称INN）；INN没有的，采用其他合适的英文名称。
    inn_name = models.CharField(max_length=100)
    # 商品名是药品生产厂商自己确定，经药品监督管理部门核准的产品名称，具有专
    # 有性质，不得仿用。在一个通用名下，由于生产厂家的不同，可有多个商品名称。
    trade_name_en = models.CharField(max_length=100,
                                     help_text='Trade Name 或Proprietary Name')
    trade_name_zh_hans = models.CharField(max_length=100)
    trade_name_pinyin = models.CharField(
        max_length=200, blank=True, null=False, default='')
    trade_name_py = models.CharField(
        max_length=200, blank=True, null=False, default='')
    # 化学名
    chemical_name_en = models.CharField(max_length=100)
    chemical_name_zh_hans = models.CharField(max_length=100)
    chemical_name_pinyin = models.CharField(
        max_length=200, blank=True, null=False, default='')
    chemical_name_py = models.CharField(
        max_length=200, blank=True, null=False, default='')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('cadn_name_py', 'cadn_name',)

    def __str__(self):
        return self.atc_code + ' : ' + self.cadn_name


class NEML(models.Model):
    """
    National Essential Medicine List 《国家基本药物目录》
    """
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(unique=True, max_length=100)


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
    name = models.CharField(unique=True, max_length=100)
