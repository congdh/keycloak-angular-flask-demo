# keycloak-angular-flask-demo

Project demo implement mô hình SPA - API tích hợp Keycloak để xác thực và phân quyền

## Keycloak

Start Keycloak server

```bash
docker-compose up -d
```

Truy cập trang quản trị `http://localhost:8180/auth/admin/` sử dụng user/password mặc định admin/admin

Import cấu hình realm từ file `realm-export.json`

## Backend OAuth2 Local Validation Example

Start backend API theo [hướng dẫn](./backend_oauth2_local_tokeninfo/README.md)

Trong keycloak, tạo client bằng cách import cấu hình client từ file [client-import-caller.json](./config/client-import-caller.json)

Start Postman, import environment `Dev` và collection `keycloak-angular-flask-demo` từ file trong thư mục postman

Trong Postman, send các request `Get token`, `Secret API` để lấy token và truy cập đến API

## Flask web

Webapp Flask (frontend + backend) sử dụng Keycload để đăng nhập, trong API gọi sang API /greeting sử dụng token của user đang đăng nhập

Trong keycloak, tạo client bằng cách import cấu hình client từ file [client-import-flask-web.json](./config/client-import-flask-web.json)

## SPA Angular 2 Service Invocation Application

Start frontend SPA theo [hướng dẫn](./app-angular2/README.md)

Frontend gọi đến 3 API của backend

- /public: Public API, không cần xác thực
- /secured: Secured API, yêu cầu user phải xác thực và có scope tương ứng (email)
- /admin: Admin API, yêu cầu user admin (TODO)

Trong keycloak, tạo client bằng cách import cấu hình client từ file [client-import-app-angular2.json.json](./config/client-import-app-angular2.json)

## Tham khảo

- https://github.com/iuliazidaru/keycloak-spring-boot-rest-angular-demo
- http://slackspace.de/articles/authentication-with-spring-boot-angularjs-and-keycloak/
- https://github.com/keycloak/keycloak/tree/master/examples/demo-template/angular-product-app