

from django.shortcuts import render, redirect, resolve_url
from django.views.generic import TemplateView, FormView, ListView
from pyperclip import copy

from petstagram_two.common.forms import CommentForm, SearchForm
from petstagram_two.common.models import Like
from petstagram_two.photos.models import Photo


# Create your views here.
class HomePage(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)

        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')
        if pet_name:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name)
        return queryset



# def home_page(request):
#     search_form = SearchForm(request.GET)
#     all_photos = Photo.objects.all()
#     if search_form.is_valid():
#         all_photos = all_photos.filter(tagged_pets__name__icontains=search_form.cleaned_data['pet_name'])
#
#
#     comment_form = CommentForm()
#     all_photos = Photo.objects.all()
#     context = {
#         'all_photos': all_photos,
#         'comment_form': comment_form,
#         'search_form': search_form,
#     }
#     return render(request, 'common/home-page.html', context)

def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id, user=request.user).first()
    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')



def copy_linc_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_id))
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

def add_comment(request, photo_id):
    if request.method == "POST":
        photo = Photo.objects.get(id=photo_id, user=request.user)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.userand
            comment.save()
        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')








