<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# Plugin DevOps Automation

Tự động hóa DevOps hoàn chỉnh cho triển khai, giám sát và ứng phó sự cố.

## Tính Năng

✅ Triển khai tự động
✅ Quy trình rollback
✅ Giám sát sức khỏe hệ thống
✅ Workflow ứng phó sự cố
✅ Tích hợp Kubernetes

## Cài Đặt

```bash
claude --plugin-dir ./07-plugins/devops-automation
```

## Những Gì Được Bao Gồm

### Lệnh Slash
- `/deploy` - Triển khai lên production hoặc staging
- `/rollback` - Rollback về phiên bản trước
- `/status` - Kiểm tra sức khỏe hệ thống
- `/incident` - Xử lý sự cố production

### Tác Nhân Con
- `deployment-specialist` - Các thao tác triển khai
- `incident-commander` - Điều phối sự cố
- `alert-analyzer` - Phân tích sức khỏe hệ thống

### MCP Server
- Tích hợp Kubernetes

### Script
- `deploy.sh` - Tự động hóa triển khai
- `rollback.sh` - Tự động hóa rollback
- `health-check.sh` - Tiện ích kiểm tra sức khỏe

### Hook
- `pre-deploy.js` - Xác thực trước khi triển khai
- `post-deploy.js` - Các tác vụ sau khi triển khai

## Cách Sử Dụng

### Triển Khai Lên Staging
```
/deploy staging
```

### Triển Khai Lên Production
```
/deploy production
```

### Rollback
```
/rollback production
```

### Kiểm Tra Trạng Thái
```
/status
```

### Xử Lý Sự Cố
```
/incident
```

## Yêu Cầu

- Claude Code 2.1+
- Kubernetes CLI (kubectl)
- Đã cấu hình quyền truy cập cluster

## Cấu Hình

Thiết lập Kubernetes config của bạn:
```bash
export KUBECONFIG=~/.kube/config
```

## Ví Dụ Workflow

```
User: /deploy production

Claude:
1. Chạy hook pre-deploy (xác thực kubectl, kết nối cluster)
2. Giao việc cho tác nhân con deployment-specialist
3. Chạy script deploy.sh
4. Giám sát tiến trình triển khai qua Kubernetes MCP
5. Chạy hook post-deploy (chờ các pod, chạy smoke test)
6. Cung cấp bản tóm tắt triển khai

Kết quả:
✅ Triển khai hoàn tất
📦 Phiên bản: v2.1.0
🚀 Pod: 3/3 sẵn sàng
⏱️  Thời gian: 2m 34s
```

---

**Cập Nhật Lần Cuối**: Ngày 18 tháng 10 năm 2026
**Phiên Bản Claude Code**: 2.1.302
**Nguồn**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**Các Mô Hình Tương Thích**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
