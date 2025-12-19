"""drf_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.clickjacking import xframe_options_exempt
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView,SpectacularJSONAPIView, SpectacularYAMLAPIView
from rest_framework import permissions


base_api = settings.BASE_API

urlpatterns = [
    # admin管理页面
    path('admin/', admin.site.urls),

    # 项目模块
    path(f'{base_api}oauth/', include('oauth.urls')),  # 用户鉴权模块
    path(f'{base_api}system/', include('system.urls')),  # 系统管理模块
    path(f'{base_api}monitor/', include('monitor.urls')),  # 系统监控模块
    path(f'{base_api}cmdb/', include('cmdb.urls')),  # 资产管理模块
    path(f'{base_api}information/', include('information.urls')),  # 个人中心模块

    # swagger(API文档)
    # JSON 格式的 OpenAPI 规范
    re_path(rf'^{base_api}swagger\.json$',
            xframe_options_exempt(SpectacularJSONAPIView.as_view()),
            name='schema-json'),

    # YAML 格式的 OpenAPI 规范
    re_path(rf'^{base_api}swagger\.yaml$',
            xframe_options_exempt(SpectacularYAMLAPIView.as_view()),
            name='schema-yaml'),

    # Swagger UI 文档界面
    path(f'{base_api}swagger/',
         xframe_options_exempt(SpectacularSwaggerView.as_view(url_name='schema')),
         name='schema-swagger-ui'),

    # ReDoc 文档界面
    path(f'{base_api}redoc/',
         xframe_options_exempt(SpectacularRedocView.as_view(url_name='schema')),
         name='schema-redoc'),

    # 通用的 schema 端点（可选，用于获取当前格式的 schema）
    path(f'{base_api}schema/',
         xframe_options_exempt(SpectacularAPIView.as_view()),
         name='schema'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
