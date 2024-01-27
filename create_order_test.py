import create_order_request
import data


def test_get_order_number_by_track():
    track = create_order_request.create_order(data.order_body).json()['track']
    response = create_order_request.get_order_number_by_track(track)
    assert response.status_code == 200
