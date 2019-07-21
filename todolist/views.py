from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import project
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from  django.forms import ModelForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
# Create your views here.







class addproject(generic.CreateView):
        model= project
        fields = "__all__"
        exclude = ['apply_date','mod_date','status']     
        
        success_url=reverse_lazy("project_query")

        template_name="pages/project_new.html"
        
       
                
        def form_invalid(self, form):        # 定义表对象没有添加失败后跳转到的页面。
                return HttpResponse("form is invalid.. this is just an HttpResponse object")




class newproject(generic.CreateView):
        model= project
        fields = "__all__"
        exclude = ['apply_date','mod_date','status']     
        
        success_url=reverse_lazy("")
        template_name="pages/project_new.html"
        def form_valid(self,form):
                form.instance.user=self.request.user
                super(newproject,self).form_valid
                return redirect("index")





# class projectdetail(generic.DetailView):
#         model= project
       
#         template_name="pages/project_detail.html"
#         context_object_name="project"

# class updateproject(generic.UpdateView):
#         model= project
#         fields = "__all__"
#         template_name="pages/project_update.html"

# class projectlist(generic.ListView):
#         model= project
        
#         template_name="pages/project_query.html"
#         context_object_name="project"


class deleteproject(generic.DeleteView):
        model= project
        
        template_name="pages/project_delete.html"
        context_object_name="project"





class projectForm(ModelForm):
    class  Meta:
        db_table = ''
        managed = True
        verbose_name = '项目'
        verbose_name_plural = 's'
        model= project
        fields = "__all__"
        exclude = ['apply_date','mod_date','status']         #排除的字段
        labels = None           #提示信息
        help_texts = None       #帮助提示信息
        widgets = None          #自定义插件
        error_messages = None   #自定义错误信息





def inform(request):
    return render(request,'pages/project_inform.html')







def projectlist(request):

    projectlist = project.objects.all()


    search_query = request.GET.get('q')
    if search_query :
                projectlist = projectlist.filter(
                        Q(projectname__icontains = search_query) |
                        Q(applicant_branch__branchname__icontains = search_query)|
                        Q(leader__icontains = search_query)|
                        Q(year__icontains = search_query)
                        
                )

    paginator = Paginator(projectlist, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    projectlist = paginator.get_page(page)




    context = {'projectlist' : projectlist}
    return render(request,'pages/project_query.html',context)



def deleteproject(request,projectid):

    delproject = project.objects.get(pk=projectid)
    delproject.delete()
    
    return redirect('project_list')


def editproject(request,projectid):

    delproject = project.objects.get(pk=projectid)
    delproject.delete()
    
    return redirect('project_query')








