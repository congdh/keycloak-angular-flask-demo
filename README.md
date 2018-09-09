# keycloak-angular-flask-demo
Project demo implement mô hình SPA - API tích hợp Keycloak để xác thực và phân quyền

## Keycloak
Start Keycloak server

```bash
docker-compose up -d
```

Truy cập trang quản trị `http://localhost:8180/auth/admin/` sử dụng user/password mặc định admin/admin

Import cấu hình realm từ file `realm-export.json`