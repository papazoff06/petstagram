from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from petstagram_two.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from petstagram_two.accounts.models import Profile
from petstagram_two.photos.models import Photo

UserModel = get_user_model()
# Create your views here.
class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')



class AppUserLoginView(LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'

    # def form_valid(self, form):
    #     super().form_valid(form)
    #     profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
    #     return HttpResponseRedirect(self.get_success_url())

class AppUserLogoutView(LogoutView):
    pass

class AppUserDetailsView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_likes_count'] = sum(p.like_set.count() for p in self.object.photo_set.all())
        context['user_photos'] = Photo.objects.filter(user_id=self.object.pk).order_by('-date_of_publication')
        return context


class ProfileEditView(UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        if self.request.user.is_authenticated:
            return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})
        return reverse_lazy('login')


# def delete_page(request, pk):
#     return render(request, 'accounts/profile-delete-page.html')
class AppUserDeleteView(DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home')
    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get)