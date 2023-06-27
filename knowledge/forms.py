from django import forms
from .models import Knowledge, Category

class KnowledgeForm(forms.ModelForm):
    class Meta:
        model = Knowledge
        fields = ('title', 'category', 'content',)

class KnowledgeCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

