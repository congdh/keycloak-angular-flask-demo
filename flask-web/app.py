import json
import logging

import requests
from flask import Flask, jsonify, current_app, g
from flask_oidc import OpenIDConnect

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False
})
oidc = OpenIDConnect(app)


@app.route('/')
def hello_world():
    if oidc.user_loggedin:
        return ('Hello, %s, <a href="/private">See private</a> '
                '<a href="/logout">Log out</a>') % \
            oidc.user_getfield('preferred_username')
    else:
        return 'Welcome anonymous, <a href="/private">Log in</a>'


@app.route('/logout')
def logout():
    """Performs local logout by removing the session cookie."""

    oidc.logout()
    return 'Hi, you have been logged out! <a href="/">Return</a>'


@app.route('/private')
@oidc.require_login
def hello_me():
    """Example for protected endpoint that extracts private information from the OpenID Connect id_token.
       Uses the accompanied access_token to access a backend service.
    """
    info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])
    username = info.get('preferred_username')
    user_id = info.get('sub')
    greeting = ''
    if user_id in oidc.credentials_store:
        try:
            from oauth2client.client import OAuth2Credentials
            access_token = OAuth2Credentials.from_json(
                oidc.credentials_store[user_id]).access_token
            # print('access_token=<%s>' % access_token)
            current_app.logger.info('access_token: <%s>' % access_token)
            headers = {'Authorization': 'Bearer %s' % (access_token)}
            # YOLO
            greeting = requests.get(
                'http://localhost:8080/greeting', headers=headers).text
        except:
            print("Could not access greeting-service")
            greeting = "Hello %s" % username
    # return ('Hello, %s! <a href="/">Return</a>' %
    #         username)
    return ("""%s, your user_id is %s!
                   <ul>
                     <li><a href="/">Home</a></li>
                     <li><a href="//localhost:8180/auth/realms/quickstart/account?referrer=flask-web&referrer_uri=http://localhost:5000/private&">Account</a></li>
                    </ul>""" %
            (greeting, user_id))


@app.route('/api', methods=['POST'])
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def hello_api():
    """OAuth 2.0 protected API endpoint accessible via AccessToken"""
    # info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])
    info = g.oidc_token_info
    return json.dumps({'hello': 'Welcome %s' % info['sub']})


if __name__ == '__main__':
    app.run()
