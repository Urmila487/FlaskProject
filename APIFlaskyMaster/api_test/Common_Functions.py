def responce_check(responce):
    if responce == 200:
        return True
    else:
        print("Response code doesn't match")
    return False


def status_check(status):
    if status == 'SUCCESS':
        return True
    else:
        print("'Status is Failure'")
    return False


def response_token_check(token):
    if type(token) == 'NULL':
        return False
    return True


def get_data_is_check(Expected_value, Actual_value):
    if Expected_value == Actual_value:
        return True
    return False


def put_response_status_is_check(putresponsestatus):
    if putresponsestatus == 'Success':
        return True
    return False




