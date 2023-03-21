from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm, AddUserForm
from webapp.models import Project


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class ProjectCreate(GroupPermission, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm
    groups = ['Project Manager', 'admin']
    success_message = 'Проект успешно создан'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(DetailView):
    template_name = 'projects/project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = self.object.issues.exclude(is_deleted=True)
        return context


class ProjectUpdate(GroupPermission, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'projects/project_update.html'
    model = Project
    form_class = ProjectForm
    groups = ['Project Manager', 'admin']
    success_message = 'Проект успешно обновлен'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(GroupPermission, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'projects/project_confirm_delete.html'
    model = Project
    groups = ['Project Manager', 'admin']
    success_message = 'Проект успешно удален'
    success_url = reverse_lazy('index')


class ProjectAddUserView(GroupPermission, PermissionRequiredMixin,  UpdateView):
    model = Project
    template_name = 'projects/projects_user_add.html'
    form_class = AddUserForm
    permission_required = 'auth.add_user'
    groups = ['Project Manager', 'Team Lead', 'admin']

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        user = form.save(commit=False)
        user.project = project
        user.save()
        form.save_m2m()
        return redirect('project_detail', pk=project.pk)

    def has_permission(self):
        return Project.objects.filter(user=self.request.user, pk=self.get_object().pk) and super().has_permission()  \
            or self.request.user.username == 'admin'
