# Example API sử dụng Oauth2

Ví dụ demo implement 1 API resource server yêu cầu sử dụng access token dưới dạng JWT + OAuth2. Ví dụ tham khảo mã nguồn từ [OAuth2 Local Validation Example](https://github.com/zalando/connexion/tree/master/examples/oauth2) của Connexion 

Running:

```bash
sudo pip3 install --upgrade connexion  # install Connexion from PyPI
./app.py
```

Now open your browser and go to http://localhost:8080/ui/ to see the Swagger UI.

You can use the hardcoded tokens to request the endpoint:

.. code-block:: bash

    $ curl http://localhost:8080/secret   # missing authentication
    $ curl -H 'Authorization: Bearer 123' http://localhost:8080/secret
    $ curl -H 'Authorization: Bearer 456' http://localhost:8080/secret

