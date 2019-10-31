import jwt
def generate_jwt(playload,private_key):
    token = jwt.encode(
        playload,
        private_key,
        algorithm='RS256')
    return token