from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Knowledge, Category
from .forms import KnowledgeForm, KnowledgeCategory

class TopView(View):
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('accounts:login')
        category_id = request.GET.get('category')
        q = request.GET.get('q')

        if category_id and q:
            knowledge_list = Knowledge.objects.filter(category_id=category_id, content__contains=q)
        elif category_id:
            knowledge_list = Knowledge.objects.filter(category_id=category_id)
        elif q:
            knowledge_list = Knowledge.objects.filter(content__contains=q)     
        else:
            knowledge_list = Knowledge.objects.all()
        categories = Category.objects.all()
        context = {'knowledge_list': knowledge_list, 'categories': categories}
        return render(request, 'knowledge/index.html', context)

class KnowledgeCategoryView(View):
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('accounts:login')
        form_category = KnowledgeCategory()
        categories = Category.objects.all()
        context = {
            'form_category': form_category, 'categories':categories,
        }
        return render(request, 'knowledge/category.html', context)

    def post(self, request, *args, **kwargs):
        form_category = KnowledgeCategory(request.POST)
        if form_category.is_valid():
            tmp = form_category.cleaned_data['name']
            if Category.objects.filter(name=tmp).exists():
                return redirect('knowledge:top')
            else:
                form_category.save()
                return redirect('knowledge:category')
        return redirect('knowledge:top')

class KnowledgeAddView(View):
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('accounts:login')
        form_add = KnowledgeForm()
        context = {
            'form_add': form_add, 
        }
        return render(request, 'knowledge/add.html', context)

    def post(self, request, *args, **kwargs):
        form_add = KnowledgeForm(request.POST)
        if form_add.is_valid():
            knowledge = form_add.save(commit=False)
            knowledge.user = self.request.user
            knowledge.save()
            return redirect('knowledge:top')
        return redirect('knowledge:top')

class KnowledgeDetailView(View):
    def get(self, request, pk):
        knowledge_detail = Knowledge.objects.get(pk=pk)
        context = {'knowledge_detail': knowledge_detail}
        return render(request, 'knowledge/detail.html', context)

class KnowledgeEditView(View):
    def get(self, request, pk):
        knowledge_detail = get_object_or_404(Knowledge, pk=pk)
        form = KnowledgeForm(instance=knowledge_detail)
        context = {'form': form}
        return render(request, 'knowledge/edit.html', context)

    def post(self, request, pk):
        knowledge_detail = get_object_or_404(Knowledge, pk=pk)
        form = KnowledgeForm(request.POST, instance=knowledge_detail)
        if form.is_valid():
            form.save()      
            return redirect('knowledge:detail', pk=knowledge_detail.pk)
        return redirect('knowledge:edit', pk=knowledge_detail.pk)

class KnowledgeDeleteView(View):
    def post(self, request, pk):
        knowledge = get_object_or_404(Knowledge, pk=pk)
        knowledge.delete()
        return redirect('knowledge:top')

class CategoryDeleteView(View):
    def post(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect('knowledge:category')
