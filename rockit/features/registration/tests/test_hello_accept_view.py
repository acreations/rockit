import uuid

from rest_framework.reverse import reverse
from rockit.features.registration.models import Member


def test_it_should_be_able_to_accept_within_two_minutes(db, client):
    hello = Member.objects.create(identifier=uuid.uuid4())

    response = client.post(reverse('hello-accept', kwargs={
        'pk': hello.identifier
    }))

    assert response