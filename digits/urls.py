from django.urls import path

from . import views

app_name = 'digits'
urlpatterns = [
    path('', views.index, name='index'),
    path('send', views.post_test, name='post_test'),
    path('predict', views.predict_image, name='predict_image'),
    path('train', views.train, name='train')
]
