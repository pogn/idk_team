from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
     url(r'^$', TemplateView.as_view(template_name = 'profile.html')), 
     url(r'^saved/', views.save_profile, name = 'saved')
]

'''
urlpatterns = [
        url(r'^profile/',views.save_profile, name='save_profile'),
        url(r'^$',views.post_list, name='post_list'),
]
'''
