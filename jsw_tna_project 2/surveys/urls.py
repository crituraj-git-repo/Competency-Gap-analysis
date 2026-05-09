from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),

    # Survey routes
    path('survey/fhq/', views.fhq, name='fhq'),
    path('survey/get/self-assessment/', views.self_assessment, {'role': 'get'}, name='get_sa'),
    path('survey/mt/self-assessment/',  views.self_assessment, {'role': 'mt'},  name='mt_sa'),
    path('survey/success/', views.success, name='success'),

    # Admin
    path('admin-login/',    views.admin_login,   name='admin_login'),
    path('admin-logout/',   views.admin_logout,  name='admin_logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-responses/<str:survey_type>/', views.admin_responses, name='admin_responses'),
    path('admin-gap-analysis/', views.gap_analysis, name='gap_analysis'),
    path('admin-export/<str:survey_type>/', views.export_excel, name='export_excel'),
]
