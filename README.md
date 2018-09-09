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

Start Postman, import environment `Dev` và collection `keycloak-angular-flask-demo` từ file trong thư mục postman

Trong Postman, send các request `Get token`, `Secret API` để lấy token và truy cập đến API