from django.contrib import admin
from django import forms
from django.core.exceptions import PermissionDenied
from .models import SvgImage, Rectangle, Tag
import logging

# Setup basic logging
logging.basicConfig(level=logging.DEBUG)


class RectangleInline(admin.TabularInline):
    model = Rectangle
    extra = 1


class SvgImageAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name='Artist').exists():
            return qs.filter(editors=request.user)
        return qs

    # def has_change_permission(self, request, obj=None):
    #     if request.user.groups.filter(name='Artist').exists():
    #         return False
    #     return super().has_change_permission(request, obj=obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='Artist').exists():
            return False
        return super().has_delete_permission(request, obj=obj)


# class SvgImageAdminForm(forms.ModelForm):
#     class Meta:
#         model = SvgImage
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         self.current_user = kwargs.pop('current_user', None)
#         super().__init__(*args, **kwargs)
#         logging.debug(f"Form initialized with current_user: {self.current_user}")
#
#     def clean(self):
#         cleaned_data = super().clean()
#         if self.instance.pk:
#             if not self.current_user:
#                 logging.error("Current user is None during form validation.")
#                 raise PermissionDenied("Current user not set.")
#             if self.current_user not in self.instance.editors.all() and not self.current_user.has_perm(
#                     'myapp.change_svgimage'):
#                 raise PermissionDenied("You do not have permission to edit this image.")
#         return cleaned_data

#
# class SvgImageAdmin(admin.ModelAdmin):
#     form = SvgImageAdminForm
#     inlines = [RectangleInline]
#     list_display = ('name', 'width', 'height')
#     list_filter = ('editors',)
#     search_fields = ('name',)
#     filter_horizontal = ('editors',)
#
#     #
#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         form.current_user = request.user
#         logging.debug(f"get_form set current_user to: {request.user}")
#         return form
#
#     #
#     def save_model(self, request, obj, form, change):
#         logging.debug(f"Saving model: {obj}, User: {request.user}, is_superuser: {request.user.is_superuser}")
#         # Allow superusers to save without additional permission checks
#         if request.user.is_superuser:
#             obj.save()
#             return
#         # Existing permission check for other users
#         if not request.user.has_perm('myapp.change_svgimage') and request.user not in obj.editors.all():
#             logging.error(f"User {request.user} does not have permission to edit this image.")
#             raise PermissionDenied("You do not have permission to edit this image.")
#         obj.save()


admin.site.register(SvgImage, SvgImageAdmin)
admin.site.register(Rectangle)
admin.site.register(Tag)
