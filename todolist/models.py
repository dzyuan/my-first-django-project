from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todolist(models.Model):
    text = models.CharField(max_length = 45)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.text


class project(models.Model):

    sort_choice=(("1","技术开发"),("2","技术引进"),("3","基础研究"),("4","软科学研究"),("5","推广应用"),)
    status_choice=(("1","编制中"),("2","审核中"),("3","通过归档"),)
    year_choice=(("2019","2019年度"),("2020","2020年度"),("2021","2021年度"),("2022","2022年度"),("2023","2023年度"),)
    projectid=models.CharField('项目编号',unique=True,max_length = 30,default='')
    projectname = models.CharField('项目名称',max_length = 30,default='')
    applicant_branch = models.ForeignKey('branch',on_delete=models.SET_NULL,null=True)
    #applicantbranch= models.CharField('申报单位',max_length = 30,default='')    
    year=models.CharField('申报年度',max_length=20,choices = year_choice,default=1)
    sort=models.CharField('项目分类',max_length = 45,choices = sort_choice,default=1)
    leader = models.CharField('负责人',max_length = 10,default='')
    personnumber= models.IntegerField('参与人数',default=0, null=True,blank=True)
    applybudget  = models.FloatField('申请资助', default=None,null=True,blank=True)
    selfbudget  = models.FloatField('自筹经费', default=None,null=True,blank=True)
    totalbudget  = models.FloatField('总预算', default=None,null=True,blank=True)
    start_date = models.DateField('开始时间', default=None, null=True,blank=True)
    complete_date = models.DateField('结束时间',  default=None, null=True,blank=True)
    apply_date = models.DateTimeField('申请时间',auto_now_add=True, null=True,blank=True)
    mod_date = models.DateTimeField('修改时间',auto_now=True, null=True,blank=True)
    purpose=models.TextField('目的',default='')
    excution=models.TextField('实施方式',default='')
    innovation=models.TextField('创新点',default='')
    status=models.CharField('项目状态',max_length=20,choices = status_choice,default=1)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    
    
    class Meta:        
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.projectname

    # def save(self, *args, **kwargs):
    #     self.user = request.User
    #     super(project, self).save(*args, **kwargs)



class branch(models.Model):
    branchname=models.CharField('单位名称',unique=True,max_length = 50,default='')
    class Meta:
        
        verbose_name = 'branch'
        verbose_name_plural = 'branches'
    def __str__(self):
        return self.branchname