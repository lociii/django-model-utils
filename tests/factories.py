import factory


class TrackedFKNullableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'tests.TrackedFKNullable'
