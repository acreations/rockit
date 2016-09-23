import uuid
from datetime import timedelta

from django.urls import reverse
from rest_framework import status
from rockit.features.registration.models import Mingle


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
    Mingle.objects.all()[0].accept()

    access_response = client.post(response.data['access'])

    assert access_response
    assert access_response.status_code is status.HTTP_200_OK
    assert access_response.data['status'] == "ACCEPT"
    assert access_response.data['token']
    assert access_response.data['refresh']

    refresh_response = client.post(access_response.data['refresh'], data={'token': access_response.data['token']})

    assert refresh_response
    assert refresh_response.status_code is status.HTTP_200_OK


def test_it_should_return_error_if_hello_request_is_blocked(db, client):
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
    Simulate block
    """
    Mingle.objects.all()[0].block()

    access_response = client.post(response.data['access'])

    assert access_response
    assert access_response.status_code is status.HTTP_404_NOT_FOUND
    assert access_response.data['status'] == "BLOCKED"


def test_it_should_return_404_if_request_is_expired(db, client):
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
    Simulate expired
    """
    hello = Mingle.objects.all()[0]
    hello.created = hello.created + timedelta(minutes=2, seconds=1)
    hello.save()

    access_response = client.post(response.data['access'])

    assert access_response
    assert access_response.status_code is status.HTTP_404_NOT_FOUND
    assert access_response.data['status'] == "EXPIRED"
