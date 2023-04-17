from django.urls import path
from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.issues import IssueCreateView, IssueDeleteView, IssueDetailView, IssueUpdateView, IssueIndexView
from webapp.views.projects import ProjectCreate, ProjectDeleteView, ProjectDetail, ProjectUpdate, ProjectAddUserView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issues/', IndexRedirectView.as_view(), name='redirect'),
    path('issues/<int:pk>', IssueDetailView.as_view(), name='issue_details'),
    path('issues/<int:pk>/update/', IssueUpdateView.as_view(), name='issue_upd'),
    path('issues/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_del'),
    path('issues/<int:pk>/confirm_delete/', IssueDeleteView.as_view(), name='issue_confirm_delete'),
    path('projects/issues/', IssueIndexView.as_view(), name='issues'),
    path('projects/add/', ProjectCreate.as_view(), name='project_add'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project_details'),
    path('projects/<int:pk>/update', ProjectUpdate.as_view(), name='project_update'),
    path('projects/<int:pk>/issue/add/', IssueCreateView.as_view(), name='add_issue'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:pk>/confirm_delete/', ProjectDeleteView.as_view(), name='project_confirm_delete'),
    path('projects/add/user/<int:pk>', ProjectAddUserView.as_view(), name='project_add_user')
]
