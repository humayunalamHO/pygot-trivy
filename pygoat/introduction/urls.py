from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('xss', views.xss,name="xss"),
    path('xssL',views.xss_lab,name='xss_lab'),
    path('xssL1',views.xss_lab,name='xss_lab'),
    path("sql",views.sql,name='sql'),
    path("sql_lab",views.sql_lab,name="sql_lab"),
    path("sql_lab1",views.sql_lab,name="sql_lab"),
    path("insec_des",views.insec_des,name="insec_des"),
    path("insec_des_lab",views.insec_des_lab,name="insec_des_lab"),
    path("xxe",views.xxe,name="xxe"),
    path("xxe_lab",views.xxe_lab,name="xxe_lab"),
    path("xxe_see",views.xxe_see,name="xxe_see"),
    path("xxe_parse",views.xxe_parse,name="xxe_parse")
]