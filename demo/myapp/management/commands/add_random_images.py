import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import SvgImage, Tag, Rectangle

class Command(BaseCommand):
    help = 'Add random images to the database'

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        tags = ['Nature', 'Art', 'Science', 'Technology']
        for tag in tags:
            Tag.objects.get_or_create(name=tag)

        for _ in range(5):
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

            # Create random rectangles for this image
            for _ in range(random.randint(1, 5)):  # Add between 1 and 10 rectangles
                Rectangle.objects.create(
                    image=svg_image,
                    x=random.randint(0, width),
                    y=random.randint(0, height),
                    width=random.randint(10, 100),
                    height=random.randint(10, 100),
                    color=f"#{random.randint(0, 0xFFFFFF):06x}"  # Random color
                )

        self.stdout.write(self.style.SUCCESS('Successfully added random images with rectangles'))
