import uuid

# crate this code to make post slug unique
def get_random_code():
    code = str(uuid.uuid4())[:11].replace("-", "")
    return code
