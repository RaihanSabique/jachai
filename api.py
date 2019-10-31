from keygeneration import key_pair_generator
from jwtgenerator import generate_jwt
from verification import verify


if __name__ == '__main__':
    private_key,public_key=key_pair_generator()
    playload={'test':'helloertiueuri',
              'test1':'h1',
              'test2':'h2ergtherhg',
              'test3': 'hellohrhf',
              'test4': 'h1wrertre',
              'test5': 'h2qythtr',
              'test6': 'helloegeth rtgrtg',
              'test7': 'h1etertb r',
              'test8': 'h2egre'
              }
    token=generate_jwt(playload,private_key)
    print('token')
    print(token)
    #public_key="-----BEGIN PUBLIC KEY----- MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCnpcZzoO/qlUDLgGWEp+BpyQzcaWl8W1GXSk4Zzme9XCTJkGQSz23kkRYg2t4rhALUR6ci28+A8jf+9Ix59hALCE3iczQwmSMlNR0rjHZH/GMKj37xOPkXAz5O6SK4MJSdwzQVLGbrPgaZyXBK08PzfqzAv9ZUBJ0Cb5S1fgtOQIDAQAB-----END PUBLIC KEY-----"
    verfied_token=verify(token,public_key)
    print('verified playload:',verfied_token)