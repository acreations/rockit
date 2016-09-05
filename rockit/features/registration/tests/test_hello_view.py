import uuid

from rest_framework import status
from rest_framework.reverse import reverse
from rockit.features.registration.models import Hello


def test_it_should_be_able_to_create_hello_request(db, client):
    data = {
        'name': 'test',
        'message': 'test message',
        'identifier': uuid.uuid4()
    }

    response = client.post(reverse('hello-list'), data)

    assert response
    assert response.status_code is status.HTTP_201_CREATED

    hellos = Hello.objects.all()

    assert len(hellos) is 1


def test_it_should_not_be_possible_to_create_more_than_one_hello(db, client):
    data = {
        'name': 'test',
        'message': 'test message',
        'identifier': uuid.uuid4()
    }

    response_one = client.post(reverse('hello-list'), data)

    response_two = client.post(reverse('hello-list'), data)

    assert response_one
    assert response_one.status_code is status.HTTP_201_CREATED
    assert response_two
    assert response_two.status_code is not status.HTTP_201_CREATED

    hellos = Hello.objects.all()

    assert len(hellos) is 1
