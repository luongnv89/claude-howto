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

Kiểm tra plugin trước khi tải:

```bash
claude plugin validate ./07-plugins/devops-automation
```

## Những Gì Được Bao Gồm

### Lệnh Slash

Lệnh của plugin được đặt namespace theo `name` của plugin trong `plugin.json`:

- `/devops-automation:deploy` - Triển khai lên production hoặc staging
- `/devops-automation:rollback` - Rollback về phiên bản trước
- `/devops-automation:status` - Kiểm tra sức khỏe hệ thống
- `/devops-automation:incident` - Xử lý sự cố production

### Tác Nhân Con
- `deployment-specialist` - Các thao tác triển khai
- `incident-commander` - Điều phối sự cố
- `alert-analyzer` - Phân tích sức khỏe hệ thống

### MCP Server

`.mcp.json` khai báo một server, `kubernetes`: npm package `mcp-server-kubernetes`, chạy bằng `npx` với `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS=true`, nên các tool xóa của nó bị tắt. Server này hiển thị là `plugin:devops-automation:kubernetes` trong `/mcp`.

### Script
- `deploy.sh` - Tự động hóa triển khai
- `rollback.sh` - Tự động hóa rollback
- `health-check.sh` - Tiện ích kiểm tra sức khỏe

### Hook

`hooks/hooks.json` đăng ký cả hai script cho các lần gọi tool Bash. Chúng chỉ tác động lên các lệnh triển khai (`deploy.sh`, `rollback.sh`, `kubectl apply`, `kubectl set image`, `kubectl rollout restart|undo`, `helm install|upgrade|rollback`) và exit 0 với mọi lệnh khác:

- `pre-deploy.js` (`PreToolUse`): chặn lệnh (exit code 2) khi thiếu `kubectl` hoặc `kubectl` không kết nối được cluster, và Claude sẽ thấy lý do
- `post-deploy.js` (`PostToolUse`): chờ tối đa 120s để các pod có nhãn `DEPLOY_APP_LABEL` sẵn sàng, và báo cho Claude nếu chúng chưa sẵn sàng. Bước chờ được bỏ qua khi chưa đặt `DEPLOY_APP_LABEL`

Cả hai hook chỉ đọc trạng thái cluster (`kubectl version`, `cluster-info`, `wait`).

## Cách Sử Dụng

### Triển Khai Lên Staging
```text
/devops-automation:deploy staging
```

### Triển Khai Lên Production
```text
/devops-automation:deploy production
```

### Rollback
```text
/devops-automation:rollback production
```

### Kiểm Tra Trạng Thái
```text
/devops-automation:status
```

### Xử Lý Sự Cố
```text
/devops-automation:incident
```

## Yêu Cầu

- Claude Code 2.1+
- Node.js (chạy các script hook và MCP server)
- Kubernetes CLI (kubectl)
- Đã cấu hình quyền truy cập cluster

## Cấu Hình

Thiết lập Kubernetes config của bạn (`.mcp.json` truyền `KUBECONFIG` cho MCP server):
```bash
export KUBECONFIG=~/.kube/config
```

Tùy chọn, cho bước kiểm tra mức sẵn sàng sau triển khai:
```bash
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## Ví Dụ Workflow

```text
User: /devops-automation:deploy production

Claude:
1. Giao việc cho tác nhân con deployment-specialist
2. Chạy script deploy.sh; hook pre-deploy kiểm tra kubectl và kết nối cluster trước
3. Giám sát tiến trình triển khai qua Kubernetes MCP
4. Hook post-deploy chờ các pod sẵn sàng
5. Cung cấp bản tóm tắt triển khai

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
