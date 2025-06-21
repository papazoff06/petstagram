from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from petstagram_two.common.forms import CommentForm
from petstagram_two.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram_two.photos.models import Photo


# Create your views here.
class PhotoAddView(CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photos/photo-add-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        foto = form.save(commit=False)
        foto.user = self.request.user
        foto.save()
        form.save_m2m()

    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})
# ---------------------------------------------
# def photo_add(request):
#     form = PhotoCreateForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return redirect('home')
#     context = {'form': form}
#     return render(request, 'photos/photo-add-page.html', context)

class PhotoDetailsView(DetailView):
    model = Photo
    template_name = 'photos/photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = self.get_object()
        photo_likes = photo.like_set.all()
        comments = photo.comment_set.all()
        comment_form = CommentForm()

        context['comments'] = comments
        context['photo_likes'] = photo_likes
        context['comment_form'] = comment_form
        context['photo'] = photo

        return context

# def photo_details(request, pk):
#     comment_form = CommentForm()
#     photo = Photo.objects.get(pk=pk)
#     photo_likes = photo.like_set.all()
#     comments = photo.comment_set.all()
#     context = {
#         'photo': photo,
#         'photo_likes': photo_likes,
#         'comments': comments,
#         'comment_form': comment_form
#     }
#     return render(request, 'photos/photo-details-page.html', context)

class PhotoEditView(UpdateView):
    model = Photo
    template_name = 'photos/photo-edit-page.html'
    form_class = PhotoEditForm
    success_url = reverse_lazy('home')

# def photo_edit(request, pk):
#     photo = Photo.objects.get(pk=pk)
#     form  = PhotoEditForm(request.POST or None, request.FILES or None, instance=photo)
#     if form.is_valid():
#         form.save()
#         return redirect('photo-details', pk)
#     context = {
#         'form': form,
#     }
#     return render(request, 'photos/photo-edit-page.html', context)

def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')


