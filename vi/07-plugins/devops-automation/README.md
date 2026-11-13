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

### Script
- `deploy.sh` - Tự động hóa triển khai
- `rollback.sh` - Tự động hóa rollback
- `health-check.sh` - Tiện ích kiểm tra sức khỏe

### Hook

`hooks/hooks.json` đăng ký cả hai script cho các lần gọi tool Bash. Chúng chỉ tác động lên các lệnh triển khai (`deploy.sh`, `rollback.sh`, `kubectl apply`, `kubectl set image`, `kubectl rollout restart|undo`, `helm install|upgrade|rollback`) và exit 0 với mọi lệnh khác:

- `pre-deploy.js` (`PreToolUse`): chặn lệnh (exit code 2) khi thiếu `kubectl` hoặc `kubectl` không kết nối được cluster, và Claude sẽ thấy lý do
- `post-deploy.js` (`PostToolUse`): kiểm tra lần triển khai và báo cho Claude nếu nó thất bại. Khi đã đặt `DEPLOY_DEPLOYMENT`, script chạy `kubectl rollout status` (tối đa 120s), lệnh này chờ các pod mới. Nếu không, khi đã đặt `DEPLOY_APP_LABEL`, script chuyển sang dùng `kubectl wait` để chờ các pod có nhãn đó ở trạng thái Ready; các pod cũ vẫn đang Ready cũng vượt qua bước kiểm tra này. Khi không đặt biến nào, bước kiểm tra được bỏ qua. Ghi chú gửi cho Claude cho biết bước kiểm tra nào đã chạy

Cả hai hook chỉ đọc trạng thái cluster (`kubectl version`, `cluster-info`, `rollout status`, `wait`).

Cách nhận diện một lệnh: các script bỏ phần thân heredoc và các chuỗi trong dấu nháy, tách lệnh theo dòng mới, `&&`, `||`, `;`, `|` và `&`, rồi xét từ đầu tiên của mỗi phần (sau `VAR=value`, các wrapper như `sudo` hoặc `env`, và các từ khóa shell như `do`, `then` hoặc `!`). Các cờ toàn cục đứng trước động từ vẫn được tính, nên `kubectl -n prod apply` và `helm -n prod upgrade` là lệnh triển khai, còn `echo "kubectl apply"`, `cat scripts/deploy.sh` và `git commit -m "helm upgrade notes"` thì không. Đây là một heuristic, không phải trình phân tích cú pháp shell: nó bỏ sót các lệnh triển khai ẩn trong dấu nháy (`bash -c "kubectl apply …"`), nằm sau các wrapper khác (`ssh`, `xargs`, `make deploy`) hoặc cờ của wrapper (`sudo -E`, `env -i`), chạy bằng `source` hoặc `.`, bắt đầu bằng đường dẫn script trong dấu nháy (`"./scripts/deploy.sh"`), nằm sau một dấu nháy chưa đóng hoặc một here-string `<<<`, hoặc bên trong các script khác. Nó cũng có thể nhận nhầm khi giá trị cờ bất thường, như `kubectl -n apply get pods`. Đừng dựa vào nó như một ranh giới an toàn.

Nếu bạn nhấn `Ctrl+Enter` trong khi một lệnh triển khai đang chạy và việc đó kết thúc lượt, hook post-deploy vẫn chạy khi lệnh hoàn tất, nhưng Claude Code sẽ dừng nó sau 10 giây, bất kể `timeout` của nó là bao nhiêu, nên bước kiểm tra có thể không hoàn tất.

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
- Node.js (chạy các script hook)
- Kubernetes CLI (kubectl)
- Đã cấu hình quyền truy cập cluster

## Cấu Hình

Các hook và script dùng cấu hình `kubectl` thông thường của bạn (`~/.kube/config`, hoặc `KUBECONFIG` nếu bạn có đặt biến này).

Tùy chọn, cho bước kiểm tra sau triển khai (đặt `DEPLOY_DEPLOYMENT`, hoặc `DEPLOY_APP_LABEL` để dùng phương án dự phòng chờ pod sẵn sàng):
```bash
export DEPLOY_DEPLOYMENT="myapp"
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## Ví Dụ Workflow

```text
User: /devops-automation:deploy production

Claude:
1. Giao việc cho tác nhân con deployment-specialist
2. Chạy script deploy.sh; hook pre-deploy kiểm tra kubectl và kết nối cluster trước
3. Hook post-deploy chờ các pod sẵn sàng
4. Cung cấp bản tóm tắt triển khai

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
**Các Mô Hình Tương Thích**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
