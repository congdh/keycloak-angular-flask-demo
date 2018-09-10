#!/usr/bin/env python3
'''
Basic example of a resource server
'''

import connexion
import jwt

# our hardcoded mock "Bearer" access tokens
TOKENS = {
    '123': 'jdoe',
    '456': 'rms'
}


def get_secret(user) -> str:
    return 'You are: {uid}'.format(uid=user)


def token_info(access_token) -> dict:
    public_key = b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqlVDBYDyxuXK+5gzQCqvimQ11UqIXdPEXwn76r1ckTxb13SfRkgL/d/UYHUDPKo+uMbamonmqilHlCfHRZzu/S+1sc9x6FemH2me9MyO24uBHx9dZEmyhK2eVuIBJ/zx5F7gWODQ+kdLVz/be8y1CG+tr4ZCCVVw1xC5WB2fDpt/N3m7kwK+KKxjjiZokLGPK8N+Ahx1tCK+iuazNHfJCEGNjt+pzEcxe8QmL53GqWLwg6GsQkGn3cbOtKH9R8oq2nX6VLt/LBkZhYZybGKJ56bOVbtvE4QHrRIH6/6xnM7pj9l4O7O9WPH1cnyM6uwYajPR4OlAX1FiiCFE8rGgswIDAQAB\n-----END PUBLIC KEY-----'
    options = {'verify_aud': False}
    decoded = jwt.decode(access_token, public_key, algorithms='RS256', options=options)
    uid = decoded.get('preferred_username')
    if not uid:
        return None
    scope = decoded.get('scope', None)
    if scope is not None:
        scope = scope.split(' ')
    else:
        scope = []
    return {'uid': uid, 'scope': scope}


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__)
    app.add_api('app.yaml')
    app.run(port=8080)
