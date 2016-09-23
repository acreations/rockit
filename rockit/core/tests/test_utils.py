import uuid

from rockit.core import utils


def test_it_should_create_a_user_since_it_does_not_exist(db):
    identifier = uuid.uuid4()

    user = utils.create_user(identifier, 'test')

    assert user.username == str(identifier)
    assert user.profile
    assert user.profile.uuid == str(identifier)
    assert user.profile.name == 'test'


def test_it_should_return_same_user_if_it_existed(db):
    user = utils.create_user(uuid.uuid4(), 'test')

    same_user = utils.create_user(user.username, 'test')

    assert user == same_user

    user.first_name = 'test'
    user.save()