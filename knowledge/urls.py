from django.urls import path
from .views import (
    TopView, 
    KnowledgeAddView,
    KnowledgeCategoryView,
    KnowledgeDetailView,
    KnowledgeEditView,
    KnowledgeDeleteView,
    CategoryDeleteView,
)

app_name = 'knowledge'

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('add/', KnowledgeAddView.as_view(), name='add'),
    path('category/', KnowledgeCategoryView.as_view(), name='category'),
    path('<int:pk>/', KnowledgeDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', KnowledgeEditView.as_view(), name='edit'),
    path('<int:pk>/delete/', KnowledgeDeleteView.as_view(), name='delete'),
    path('<int:pk>/delete_category/', CategoryDeleteView.as_view(), name='delete_category'),   
]
