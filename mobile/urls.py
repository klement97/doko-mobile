from django.urls import path

from mobile.views import ManagerPageView, RegisterView, EmailDeleteView, EmailUpdateView, read, validate_email

urlpatterns = [
    path('', RegisterView.as_view(), name='home'),
    path('manager/', ManagerPageView.as_view(), name='manager'),
    path('register/', RegisterView.as_view(), name='register'),
    path('manager/email/delete/<int:pk>', EmailDeleteView.as_view(), name='delete_email'),
    path('manager/email/update/<int:pk>', EmailUpdateView.as_view(), name='update_email'),
    path('ajax/read/', read, name='read'),
    path('ajax/validate_email/', validate_email, name='validate_email'),
]
