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


def get_greeting(user) -> str:
    return 'Hello {user}'.format(user=user)


def get_public() -> str:
    return 'Public'


def token_info(access_token) -> dict:
    public_key = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrVrCuTtArbgaZzL1hvh0xtL5mc7o0NqPVnYXkLvgcwiC3BjLGw1tGEGoJaXDuSaRllobm53JBhjx33UNv+5z/UMG4kytBWxheNVKnL6GgqlNabMaFfPLPCF8kAgKnsi79NMo+n6KnSY8YeUmec/p2vjO2NjsSAVcWEQMVhJ31LwIDAQAB\n-----END PUBLIC KEY-----'
    options = {'verify_aud': False}
    decoded = jwt.decode(access_token, public_key,
                         algorithms='RS256', options=options)
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
