import uuid

from django.urls import reverse
from rest_framework import status
from rockit.features.registration.models import Member


def test_it_should_poll_for_access_if_hello_is_not_more_than_2_minutes_old(db, client):
    data = {
        'name': 'test',
        'message': 'test message',
        'identifier': uuid.uuid4()
    }

    response = client.post(reverse('hello-list'), data)

    assert response
    assert response.status_code is status.HTTP_201_CREATED

    """
    Try to poll once
    """
    access_response = client.post(response.data['access'])

    assert access_response
    assert access_response.status_code is status.HTTP_200_OK
    assert access_response.data['status'] == "WAITING"

    """
    Simulate an accept
    """
    Member.objects.all()[0].accept()

    access_response = client.post(response.data['access'])

    assert access_response
    assert access_response.status_code is status.HTTP_200_OK
    assert access_response.data['status'] == "ACCEPT"