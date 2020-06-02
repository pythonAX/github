from django.urls import path,re_path
from . import views
urlpatterns = [
    path('makr/',views.Create_makr.as_view()),
    re_path("^makr/(?P<pk>\d+)/(?P<start>\d+)/(?P<end>\d+)/$",views.Get_makr.as_view()),
    re_path("^makr/(?P<pk>\d+)/$",views.Get_makr.as_view())

]