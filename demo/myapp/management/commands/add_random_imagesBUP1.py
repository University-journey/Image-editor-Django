# add_random_images.py
import random
from django.core.management.base import BaseCommand
from ...models import SvgImage, Tag
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Add random images to the database'

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        tags = ['Nature', 'Art', 'Science', 'Technology']
        for tag in tags:
            Tag.objects.get_or_create(name=tag)

        for _ in range(10):
            name = f"Image_{random.randint(1, 1000)}"
            width = random.randint(100, 1000)
            height = random.randint(100, 1000)
            description = f"This is a description for {name}"
            svg_image = SvgImage.objects.create(
                name=name,
                width=width,
                height=height,
                description=description
            )
            svg_image.editors.set(random.sample(users, k=random.randint(1, len(users))))
            svg_image.tags.set(Tag.objects.order_by('?')[:random.randint(1, 3)])
            svg_image.save()

        self.stdout.write(self.style.SUCCESS('Successfully added random images'))