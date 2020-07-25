
from django.contrib import admin
from django.urls import path, include
from . import views
import account.urls
import content.urls

urlpatterns = [
    path('<int:post_id>', views.detail, name="detail"),
    path('list/', views.list, name="list"),
    path('new/', views.new, name="new"),
    path('edit/<int:post_id>', views.edit, name="edit"),
    path('delete/<int:post_id>', views.delete, name="delete"),
    path('new_comment/<int:post_id>', views.new_comment, name="new_comment"),
    path('del_comment/<int:comment_id>', views.del_comment, name="del_comment"),
]
