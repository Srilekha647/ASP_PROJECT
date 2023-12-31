from django.urls import path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('me/', views.dashboard, name='dashboard'),
    path('me/article/create/', views.create_post, name='article-create'),
    path('me/published-articles/', views.published_articles, name='published-articles'),
    path('me/drafted-articles/', views.drafted_articles, name='drafted-articles'),
    path('me/profile/', views.author_profile, name='author-profile'),
    path('me/settings/', views.author_settings, name='author-settings'),
    path('me/<slug:slug>/', views.post_details, name='post_details'),
    path('me/edit/<slug:slug>/', views.edit_magazine_post, name='edit-post'),
    path('me/delete/<slug:slug>/', views.delete_post, name='delete-post'),
    path('me/add/category/', views.create_category, name='add-category'),
    path('me/add/tag/', views.tags_view, name='add-tag')
]
