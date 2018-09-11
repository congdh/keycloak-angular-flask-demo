#!/usr/bin/env python3
"""
Basic example of a resource server
"""
import sys

import connexion
import jwt
from flask_cors import CORS
import logging
from flask import jsonify, current_app

logging.getLogger('flask_cors').level = logging.DEBUG


def get_secret(user) -> str:
    return 'You are: {uid}'.format(uid=user)


def get_greeting(user) -> str:
    return 'Hello {user}'.format(user=user)


def get_public() -> str:
    return jsonify(message='Public')


def get_secured() -> str:
    return jsonify(message='Secured')


def get_admin() -> str:
    return jsonify(message='Admin')


def token_info(access_token) -> dict:
    public_key = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrVrCuTtArbgaZzL1hvh0xtL5mc7o0NqPVnYXkLvgcwiC3BjLGw1tGEGoJaXDuSaRllobm53JBhjx33UNv+5z/UMG4kytBWxheNVKnL6GgqlNabMaFfPLPCF8kAgKnsi79NMo+n6KnSY8YeUmec/p2vjO2NjsSAVcWEQMVhJ31LwIDAQAB\n-----END PUBLIC KEY-----'
    current_app.logger.debug('Access token: {access_token}'.format(access_token=access_token))
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
    # add CORS support
    CORS(app.app)

    handler_console = logging.StreamHandler(stream=sys.stdout)
    logger = logging.getLogger('connexion.apis')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler_console)

    logger = logging.getLogger('connexion.api.security')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler_console)

    logger = app.app.logger
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler_console)

    app.run(port=8080)
