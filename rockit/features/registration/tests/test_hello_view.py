from rest_framework.reverse import reverse


def test_it_should_be_able_to_create_hello_request(db, client):
    response = client.get(reverse('hello-list'))

    assert response