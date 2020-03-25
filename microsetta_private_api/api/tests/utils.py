import json


def check_response(response, expected_status=None):
    if expected_status is not None:
        assert response.status_code == expected_status
    elif response.status_code >= 400:
        print(response.data)
        raise Exception("Scary response code: " + str(response.status_code))

    if response.status_code == 204 and len(response.data) == 0:
        # No content to check.
        pass
    elif response.headers.get("Content-Type") == "application/json":
        resp_obj = json.loads(response.data)
        if isinstance(resp_obj, dict) and "message" in resp_obj:
            msg = resp_obj["message"].lower()
            if "not" in msg and "implemented" in msg:
                raise Exception(response.data)
