from rest_framework.reverse import reverse


def test_it_should_contain_hello(client):
    response = client.get(reverse('registration'))

    assert response
    assert response.status_code is 200
    assert 'hello' in response.data