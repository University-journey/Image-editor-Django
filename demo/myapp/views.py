# views.py
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SvgImage, Rectangle, Tag
from .forms import RectangleForm

def image_list(request):
    images = SvgImage.objects.all().order_by('id')  # Ensure queryset is ordered

    # Filtering by tags
    tag = request.GET.get('tag')
    if tag:
        images = images.filter(tags__name=tag)

    # Sorting by publication date
    sort = request.GET.get('sort')
    if sort == 'asc':
        images = images.order_by('publication_date')
    elif sort == 'desc':
        images = images.order_by('-publication_date')

    # Pagination
    paginator = Paginator(images, 10)  # Show 10 images per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'image_list.html', {'page_obj': page_obj, 'tags': Tag.objects.all()})

def image_detail(request, id):
    image = get_object_or_404(SvgImage, id=id)
    rectangles = image.rectangles.all()

    # Check if the user can edit the image
    can_edit = request.user in image.editors.all() and request.user.has_perm('myapp.change_svgimage')
    can_delete = request.user in image.editors.all() and request.user.has_perm('myapp.delete_svgimage')

    if request.method == 'POST':
        if 'delete' in request.POST and can_delete:
            rect_id_to_delete = request.POST.get('delete')
            if rect_id_to_delete:
                Rectangle.objects.filter(id=rect_id_to_delete).delete()
        elif 'add' in request.POST and can_edit:
            form = RectangleForm(request.POST)
            if form.is_valid():
                new_rect = form.save(commit=False)
                new_rect.image = image
                new_rect.save()
        return redirect('image_detail', id=id)
    else:
        form = RectangleForm()

    return render(request, 'image_detail.html', {
        'image': image,
        'form': form,
        'rectangles': rectangles,
        'can_edit': can_edit,
        'can_delete': can_delete
    })
