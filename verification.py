import traceback

import jwt
def verify(token,public_key):
    try:
        return jwt.decode(token, public_key, algorithms=['RS256'])
    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())
        return "Verification failed"
