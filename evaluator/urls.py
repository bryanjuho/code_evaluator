from django.urls import path
from .views import *

app_name = 'evaluator'

urlpatterns = [
    path('', ClassList.as_view(), name='class_list'),
    path('detail/<int:pk>/', ClassDetail.as_view(), name='class_detail'),
    path('create/', ClassCreate.as_view(), name='class_create'),
    path('join/', ClassJoin.as_view(), name='class_join'),
    path('students/', StudentList.as_view(), ),
    path('result/<int:pk>/', EvaluationResult.as_view(), name='result'),
    path('statistics/<int:pk>/', AssignmentStatistics.as_view(), name='statistics'),
    path('assignment/<int:pk>/', AssignmentNotice.as_view(), name='assignment_notice'),
    path('assignment/<int:assignment_pk>/submit/', SubmissionCreate.as_view(), name='submission_create'),
    # path('assignment/<int:assignment_pk>/update/<int:pk>/', SubmissionUpdate.as_view(), name='submission_update'),
    path('assignment/<int:pk>/create/', AssignmentCreate.as_view(), name='assignment_create'),
    path('assignment/<int:pk>/edit/', AssignmentEdit.as_view(), name='assignment_edit'),
    path('document/<int:document_id>/', FileDownloadView.as_view(), name="download"),
]
