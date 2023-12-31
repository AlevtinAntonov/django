from django.urls import path

from s3app import views

app_name = 's3app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('heads_game/<int:count>', views.HeadsGame.as_view(), name='heads_game'),
    path('dice_game/<int:count>', views.DiceGame.as_view(), name='dice_game'),
    path('articles/<int:pk>', views.AllArticlesView.as_view(), name='articles'),
    path('article/<int:pk>', views.ArticlePage.as_view(), name='article_page'),
    path('heads/', views.heads, name='heads'),
    path('last/', views.last_games, name='last_games'),
    path('author/', views.authors, name='author'),
]