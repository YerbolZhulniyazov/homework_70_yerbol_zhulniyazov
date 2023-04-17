from django.urls import path
from api.views import ProjectDetailView, IssueDetailView, ProjectUpdateView, \
    IssueUpdateView, ProjectDeleteView, IssueDeleteView


urlpatterns = [
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('issue/<int:pk>', IssueDetailView.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update/', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete')

]
