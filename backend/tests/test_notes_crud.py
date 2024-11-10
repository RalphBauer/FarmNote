import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from fastapi.testclient import TestClient
from datetime import datetime, timedelta
from app.main import app


# test fixture --------------------------------------------------------------

client = TestClient(app)

invalid_test_token = '123456'
test_token = 'FHXIKD'
test_note_id = 0


def parse_datetime(value):
    return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

# ---------------------------------------------------------------------------


def test_create_note_success():
    global test_note_id
    response = client.post('/notes/',
                            json={
                                'content': 'My first note',
                                'latitude': 48.1271,
                                'longitude': 15.1247,
                                'field_id': 0
                            }, params={
                                'token': test_token
                            }
                           )

    x = response.json()

    test_note_id = x['id']

    assert response.status_code == 200
    assert x['content'] == 'My first note'
    assert x['latitude'] == 48.1271
    assert x['longitude'] == 15.1247
    assert x['field_id'] == 0
    assert x['id'] >= 0, 'note id should be greater or equal than 0'
    assert x['session_id'] >= 0, 'session id should be greater or equal than 0'
    assert (parse_datetime(x['creation_date']) > (datetime.utcnow() - timedelta(minutes=1))) == True, 'creation_date should be the current time'
    assert x['updated_date'] == x['creation_date'], 'updated_date should equal the creation_date'


def test_read_notes_success():
    response = client.get('/notes/',
                           params={
                                'token': test_token
                            }
                           )

    json_result = response.json()

    assert response.status_code == 200
    assert len(json_result) == 1, 'only one note should be returned'
    assert all([json_result[0][x] == y for x, y in zip(['content', 'latitude', 'longitude'], ['My first note', 48.1271, 15.1247])])


def test_read_notes_token_not_found():
    response = client.get('/notes/',
                           params={
                                'token': invalid_test_token
                            }
                           )

    assert response.status_code == 401, 'should return status code 401 - invalid token'


def test_read_note_success():
    response = client.get(f'/notes/{test_note_id}',
                           params={
                                'token': test_token
                            }
                           )

    json_result = response.json()

    assert response.status_code == 200
    assert json_result['content'] == 'My first note'
    assert json_result['latitude'] == 48.1271
    assert json_result['longitude'] == 15.1247
    assert json_result['field_id'] == 0


def test_read_note_token_not_found():
    response = client.get(f'/notes/{test_note_id}',
                           params={
                                'token': invalid_test_token
                            }
                           )

    assert response.status_code == 401, 'should return status code 401 - invalid token'


def test_read_note_not_found():
    response = client.get(f'/notes/42000000',
                           params={
                                'token': test_token
                            }
                           )

    assert response.status_code == 404, 'should return status code 404 - not found'


def test_update_note_success():
    response = client.put(f'/notes/{test_note_id}',
                              json={
                                  'content': 'Update',
                                  'latitude': 48.5,
                                  'longitude': 15.4,
                                  'field_id': 5
                              },
                              params={
                                  'token': test_token
                              }
                           )

    json_result = response.json()

    assert response.status_code == 200
    assert json_result['content'] == 'Update'
    assert json_result['latitude'] == 48.5
    assert json_result['longitude'] == 15.4
    assert json_result['field_id'] == 5

    response = client.get(f'/notes/{test_note_id}',
                              params={
                                  'token': test_token
                              }
                          )

    json_result = response.json()

    assert response.status_code == 200
    assert json_result['content'] == 'Update'
    assert json_result['latitude'] == 48.5
    assert json_result['longitude'] == 15.4
    assert json_result['field_id'] == 5


def test_update_note_token_not_found():
    response = client.put(f'/notes/{test_note_id}',
                              json={
                                  'content': 'Update',
                                  'latitude': 48.5,
                                  'longitude': 15.4,
                                  'field_id': 5
                              },
                              params={
                                  'token': invalid_test_token
                              }
                           )

    assert response.status_code == 401, 'should return status code 401 - invalid token'


def test_update_note_not_found():
    response = client.put(f'/notes/42000000',
                              json={
                                  'content': 'Update',
                                  'latitude': 48.5,
                                  'longitude': 15.4,
                                  'field_id': 5
                              },
                              params={
                                  'token': test_token
                              }
                           )

    assert response.status_code == 404, 'should return status code 404 - not found'


def test_delete_note_success():
    response = client.delete(f'/notes/{test_note_id}',
                              params={
                                  'token': test_token
                              }
                           )

    assert response.status_code == 200, 'should return status code 200 if deletion was successful'

    response = client.get(f'/notes/{test_note_id}',
                          params={
                              'token': test_token
                          }
                          )

    assert response.status_code == 404, 'should return status code 404 - not found'


def test_delete_note_not_found():
    response = client.delete(f'/notes/42000000',
                              params={
                                  'token': test_token
                              }
                           )

    assert response.status_code == 404, 'should return status code 404 - not found'


def test_delete_note_token_not_found():
    response = client.delete(f'/notes/{test_note_id}',
                              params={
                                  'token': invalid_test_token
                              }
                           )

    assert response.status_code == 401, 'should return status code 401 - invalid token'

def test_create_note_invalid_input():
    response = client.post('/notes/',
                           json={
                               'content': 'My first note',  # Valid field
                               # 'latitude' is missing (invalid input)
                               'longitude': 15.1247,
                               'field_id': 0
                           }, params={
            'token': test_token
        }
                           )

    assert response.status_code == 422, 'should return status code 422 - invalid input'
    assert 'detail' in response.json(), 'should return a detail message about the validation error'


    response = client.post('/notes/',
                           json={
                               'content': 'My first note',
                               'latitude': 48.5,
                               'longitude': 15.1247,
                               'field_id': -1
                           }, params={
            'token': test_token
        }
                           )

    assert response.status_code == 422, 'should return status code 422 - invalid input'
    assert 'detail' in response.json(), 'should return a detail message about the validation error'


    response = client.post('/notes/',
                           json={
                               'content': 'My first note',
                               'latitude': 48.5,
                               'longitude': -1,
                               'field_id': 8
                           }, params={
            'token': test_token
        }
                       )

    assert response.status_code == 422, 'should return status code 422 - invalid input'
    assert 'detail' in response.json(), 'should return a detail message about the validation error'


    response = client.post('/notes/',
                           json={
                               'content': 'My first note',
                               'latitude': -1,
                               'longitude': 15.1245,
                               'field_id': 8
                           }, params={
            'token': test_token
        }
                           )

    assert response.status_code == 422, 'should return status code 422 - invalid input'
    assert 'detail' in response.json(), 'should return a detail message about the validation error'

