"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sign import views   #导入sign应用导入views文件

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index), #添加index/路径配置
    url(r'^login_action/$',views.login_action),#配置login_action交易路由
    url(r'^event_manage/$',views.event_manage),#配置event_manage路由
    url(r'^accounts/login/$',views.index),#配置accounts路由，出错后直接返回登陆页面
    url(r'^Event_search_name/$',views.Event_search_name),
    url(r'^wxj/$',views.wxj),
    url(r'^guest_manage/$',views.guest_manage),
    url(r'^logout/$',views.logout),
    url(r'^Guest_search_name/$',views.Guest_serch_name),
    url(r'^sign_index/(?P<eid>[0-9]+)/$',views.sign_index),#定义签到会的页面，(?P<eid>[0-9]+)匹配签到会的id
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$',views.sign_index_action),
]



