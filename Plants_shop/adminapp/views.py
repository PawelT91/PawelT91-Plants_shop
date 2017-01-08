from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from usermanagementapp.forms import MyRegistrationForm, UserChangeForm
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.template import loader
from django.http import Http404, JsonResponse
from django.template.context_processors import csrf
from mainapp.models import CactusGenus, ViewCactus
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

@user_passes_test(lambda u: u.is_superuser)
def admin_main(request):
    users = User.objects.all()
    user_form = MyRegistrationForm()
    return render(request, 'admin_page.html', {'users': users, 'form': user_form})


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin')


def get_user_form(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, id=user_id)
        user_form = MyRegistrationForm(instance=user)
        context = {'form': user_form, 'id': user_id}
        context.update(csrf(request))
        html = loader.render_to_string('inc-registration_form.html', context)
        data = {'errors': False, 'html': html}
        return JsonResponse(data)
    raise Http404


def create_user(request, user_id=None):
    if request.is_ajax():
        if not user_id:
            form = MyRegistrationForm(request.POST)
        else:
            user = get_object_or_404(User, id=user_id)
            form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            users = User.objects.all()
            html = loader.render_to_string('inc-users_list.html', {'users': users}, request=request)
            data = {'errors': False, 'html': html}
            return JsonResponse(data)
        else:
            errors = user.errors.as_json()
            return JsonResponse({'errors': errors})
    raise Http404


class GensListView(ListView):
    model = CactusGenus
    template_name = 'admin_genus.html'
    paginate_by = 10


class GensDetailView(DetailView):
    model = CactusGenus
    template_name = 'admin_genus_detail.html'


class GensCreateView(CreateView):
    model = CactusGenus
    template_name = 'admin_genus_create.html'
    success_url = '/admin/genus'
    fields = ('__all__')


class GensUpdateView(UpdateView):
    model = CactusGenus
    template_name = 'admin_genus_update.html'
    success_url = '/admin/genus'
    fields = ('__all__')


class GensDeleteView(DeleteView):
    model = CactusGenus
    success_url = '/admin/view'
    template_name = 'confirm_delete.html'

# Виды


class ViewsListView(ListView):
    model = ViewCactus
    template_name = 'admin_view.html'
    paginate_by = 10


class ViewsDetailView(DetailView):
    model = ViewCactus
    template_name = 'admin_genus_detail.html'


class ViewsCreateView(CreateView):
    model = ViewCactus
    template_name = 'admin_genus_create.html'
    success_url = '/admin/view'
    fields = ('__all__')


class ViewsUpdateView(UpdateView):
    model = ViewCactus
    template_name = 'admin_genus_update.html'
    success_url = '/admin/view'
    fields = ('__all__')


class ViewsDeleteView(DeleteView):
    model = ViewCactus
    success_url = '/admin/view'
    template_name = 'confirm_delete.html'