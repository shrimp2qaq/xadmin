#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
#课程
class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name='课程名')
    desc = models.CharField(max_length=300,verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(choices=(('cj','初级'),('zj','中级'),('gj','高级')),max_length=2)
    learn_times = models.IntegerField(default=0,verbose_name='学习时长(分钟数)')
    students = models.IntegerField(default=0,verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0,verbose_name='收藏人数')
    image = models.ImageField(upload_to='course/%Y/M',verbose_name='封面图片',max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间',)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):#重载Unicode方法来让数据在其他地方显示你想要的名字
        return self.name

#章节
class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程')
    name = models.CharField(max_length=100,verbose_name='章节名')
    add_time = models.DateTimeField(default= datetime.now,verbose_name ='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name='章节')
    name = models.CharField(max_length=100,verbose_name='视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', )

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='名称')
    download = models.FileField(upload_to='course/resource/%Y/%M',verbose_name='资源文件',max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name