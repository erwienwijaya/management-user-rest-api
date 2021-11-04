import uuid

def make_code():
    code = str(uuid.uuid4()).replace("-","")[:16]
    return code