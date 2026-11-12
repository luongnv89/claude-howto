# Ví Dụ Về Checkpoint

Các ví dụ thực tế về cách sử dụng checkpoint hiệu quả trong Claude Code.

Lưu ý: Checkpoint được tạo tự động với mỗi prompt của người dùng. Bạn không cần lưu chúng thủ công. Để quay lại (rewind), nhấn `Esc` hai lần (`Esc+Esc`) hoặc dùng `/rewind` để mở trình duyệt checkpoint.

## Ví Dụ 1: Di Chuyển Cơ Sở Dữ Liệu

### Tình Huống
Bạn cần di chuyển từ MySQL sang PostgreSQL nhưng muốn thử cả hai cách: di chuyển trực tiếp và di chuyển dần dần với ghi kép (dual-write).

### Workflow

```
User: Hãy triển khai di chuyển trực tiếp từ MySQL sang PostgreSQL
      [Checkpoint A được tạo tự động]

Claude: Tôi sẽ triển khai di chuyển trực tiếp...
[Đổi database driver, cập nhật các truy vấn, sửa schema]

User: Chạy test
      [Checkpoint B được tạo tự động]

Claude: Đang chạy test...
❌ 15 test thất bại - lỗi connection pool

User: Cách này có vấn đề. Hãy thử mẫu dual-write thay thế.
[Người dùng nhấn Esc+Esc, chọn Checkpoint A, chọn "Restore code and conversation"]

User: Giờ hãy triển khai mẫu dual-write, ghi vào cả hai cơ sở dữ liệu

Claude: Tôi sẽ triển khai di chuyển dual-write...
[Triển khai tầng dual-write, chiến lược di chuyển dần dần]

User: Chạy test

Claude: Đang chạy test...
✅ Tất cả test đều pass

User: Cách dual-write rõ ràng an toàn hơn. Hãy commit cái này.
```

## Ví Dụ 2: Tối Ưu Hiệu Năng

### Tình Huống
Có nhiều chiến lược tối ưu hiệu năng cần thử.

### Workflow

```
User: Hãy tối ưu thời gian phản hồi API. Hiện tại: 450ms
      [Checkpoint "Baseline" được tạo tự động]

Claude: Tôi sẽ thêm caching cho truy vấn cơ sở dữ liệu...
[Triển khai caching bằng Redis]

User: Chạy test hiệu năng

Claude: Kết quả: thời gian phản hồi trung bình 280ms (cải thiện 38%)

User: Để tôi thử một cách khác.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Baseline", chọn "Restore code and conversation"]

User: Thay vào đó hãy thử tối ưu truy vấn cơ sở dữ liệu

Claude: Tôi sẽ tối ưu các truy vấn cơ sở dữ liệu...
[Thêm index, tối ưu các truy vấn N+1]

User: Chạy test hiệu năng

Claude: Kết quả: thời gian phản hồi trung bình 180ms (cải thiện 60%)

User: Để tôi thử thêm cách thứ ba.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Baseline", chọn "Restore code and conversation"]

User: Thử nén response và CDN

Claude: Tôi sẽ thêm nén và CDN...
[Triển khai gzip, thiết lập CDN]

User: Chạy test hiệu năng

Claude: Kết quả: thời gian phản hồi trung bình 320ms (cải thiện 29%)

User: Tối ưu truy vấn là tốt nhất. Để tôi quay lại và kết hợp nó với caching.
[Người dùng nhấn Esc+Esc, chọn checkpoint sau bước tối ưu truy vấn, chọn "Restore code and conversation"]

User: Giờ hãy thêm Redis caching lên trên các truy vấn đã tối ưu này

Claude: [Thêm Redis caching lên trên các truy vấn đã tối ưu]

User: Chạy test hiệu năng

Claude: Kết quả: thời gian phản hồi trung bình 95ms (cải thiện 79%) 🎉

User: Hoàn hảo! Đây là phương án thắng. Hãy commit cái này.
```

## Ví Dụ 3: Lặp Lại Thiết Kế UI/UX

### Tình Huống
Thử các bố cục khác nhau cho một dashboard.

### Workflow

```
User: Hãy thiết kế lại dashboard với bố cục sidebar
      [Checkpoint "Start" được tạo tự động]

Claude: [Triển khai bố cục sidebar]

User: Cho tôi xem ảnh chụp màn hình

Claude: [Hiển thị ảnh chụp màn hình]

User: Sidebar có vẻ chật chội. Hãy thử thanh điều hướng trên cùng thay thế.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Start", chọn "Restore code and conversation"]

User: Thử bố cục điều hướng trên cùng

Claude: [Triển khai điều hướng trên cùng]

User: Cho tôi xem ảnh chụp màn hình

Claude: [Hiển thị ảnh chụp màn hình]

User: Tốt hơn, nhưng hãy thử bố cục lưới dạng thẻ (card)
[Người dùng nhấn Esc+Esc, chọn checkpoint "Start", chọn "Restore code and conversation"]

User: Thử bố cục lưới dạng thẻ

Claude: [Triển khai lưới thẻ]

User: Cho tôi xem ảnh chụp màn hình

Claude: [Hiển thị ảnh chụp màn hình]

User: Tuyệt vời! Nhưng ta có thể kết hợp điều hướng trên cùng với lưới thẻ không?
[Người dùng nhấn Esc+Esc, chọn checkpoint sau bước lưới thẻ, chọn "Restore code and conversation"]

User: Thêm điều hướng trên cùng vào bố cục lưới thẻ

Claude: [Thêm điều hướng trên cùng vào lưới thẻ]

User: Hoàn hảo! Đây là thiết kế cuối cùng.
```

## Ví Dụ 4: Phiên Gỡ Lỗi

### Tình Huống
Truy tìm một lỗi khó với nhiều giả thuyết.

### Workflow

```
User: Ứng dụng đang bị rò rỉ bộ nhớ
      [Checkpoint "Before debugging" được tạo tự động]

Claude: Để tôi điều tra...
[Phân tích code]

User: Tôi nghĩ lỗi nằm ở các event listener. Hãy sửa chúng.

Claude: [Sửa phần dọn dẹp event listener]

User: Chạy memory profiler

Claude: Vẫn rò rỉ bộ nhớ - event listener không phải nguyên nhân

User: Để tôi quay lại và thử một giả thuyết khác.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Before debugging", chọn "Restore code and conversation"]

User: Có thể là do kết nối cơ sở dữ liệu?

Claude: [Triển khai các bản sửa cho connection pooling]

User: Chạy memory profiler

Claude: Vẫn rò rỉ - cũng không phải do kết nối

User: Để tôi quay lại và thử một hướng khác.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Before debugging", chọn "Restore code and conversation"]

User: Hãy kiểm tra tham chiếu vòng (circular reference)

Claude: [Tìm và sửa tham chiếu vòng trong cache]

User: Chạy memory profiler

Claude: ✅ Đã sửa rò rỉ bộ nhớ! Thủ phạm là các tham chiếu vòng trong tầng caching.

User: Xuất sắc! Hãy commit bản sửa này.
```

## Ví Dụ 5: Tiến Hóa Thiết Kế API

### Tình Huống
Thiết kế một REST API qua nhiều vòng lặp.

### Workflow

```
User: Tạo một REST API cho nền tảng blog của chúng ta
      [Checkpoint "Before API design" được tạo tự động]

Claude: [Tạo CRUD API cơ bản]

User: Cái này quá đơn giản. Hãy thêm phân trang và lọc

Claude: [Thêm phân trang và lọc]

User: Chúng ta cần quan hệ tài nguyên tốt hơn

Claude: [Triển khai link HATEOAS]

User: Thật ra, hãy thử GraphQL thay vì REST
[Người dùng nhấn Esc+Esc, chọn checkpoint "Before API design", chọn "Restore code and conversation"]

User: Thay vào đó hãy triển khai GraphQL API cho nền tảng blog của chúng ta

Claude: [Triển khai GraphQL API]

User: Tôi nghĩ REST phù hợp hơn với trường hợp của chúng ta.
[Người dùng nhấn Esc+Esc, chọn checkpoint sau bước HATEOAS, chọn "Restore code and conversation"]

User: Hãy hoàn thiện cách tiếp cận REST.
```

## Ví Dụ 6: Quản Lý Cấu Hình

### Tình Huống
Thử nghiệm các cách tiếp cận cấu hình khác nhau.

### Workflow

```
User: Chuyển cấu hình sang biến môi trường
      [Checkpoint "Original config" được tạo tự động]

Claude: [Triển khai cấu hình bằng biến môi trường]

User: Test trong môi trường development

Claude: Chạy được ở local nhưng có vấn đề khi deploy lên production

User: Để tôi thử một cách khác.
[Người dùng nhấn Esc+Esc, chọn checkpoint "Original config", chọn "Restore code and conversation"]

User: Thử cách dùng file cấu hình có validation

Claude: [Triển khai cấu hình YAML với validation bằng JSON schema]

User: Test trong môi trường development

Claude: ✅ Chạy tốt, thông báo lỗi validation rõ ràng

User: Ta có thể hỗ trợ thêm biến môi trường cho các giá trị nhạy cảm không?

Claude: [Thêm ghi đè bằng biến môi trường cho các secret]

User: Test deploy

Claude: ✅ Tất cả môi trường đều hoạt động đúng

User: Hoàn hảo! Cái này đã sẵn sàng cho production.
```

## Ví Dụ 7: Chiến Lược Kiểm Thử

### Tình Huống
Triển khai kiểm thử toàn diện.

### Workflow

```
User: Thêm unit test cho module auth
      [Checkpoint được tạo tự động]

Claude: [Thêm unit test bằng Jest]

User: Chạy test

Claude: 45 test pass, độ bao phủ 78%

User: Thêm cả integration test nữa

Claude: [Thêm integration test]

User: Chạy test

Claude: 89 test pass, độ bao phủ 92%, nhưng test chạy chậm (3 phút)

User: Test chạy chậm quá. Hãy tối ưu.

Claude: [Tối ưu phần thiết lập test, thêm chạy song song]

User: Chạy test

Claude: 89 test pass, độ bao phủ 92%, 35 giây ✅

User: Tuyệt! Giờ thêm E2E test cho các luồng quan trọng

Claude: [Thêm E2E test bằng Playwright]

User: Chạy tất cả test

Claude: 112 test pass, độ bao phủ 94%, 2 phút

User: Cân bằng hoàn hảo giữa độ bao phủ và tốc độ!
```

## Ví Dụ 8: Dùng Summarize Từ Checkpoint

### Tình Huống
Sau một phiên gỡ lỗi dài, bạn muốn rút gọn cuộc hội thoại mà vẫn giữ được ngữ cảnh.

### Workflow

```
User: [Sau hơn 20 tin nhắn gỡ lỗi và khám phá]

[Người dùng nhấn Esc+Esc, chọn một checkpoint sớm, chọn "Summarize from here"]
[Có thể kèm hướng dẫn: "Tập trung vào những gì ta đã thử và cái gì hiệu quả"]

Claude: [Tạo bản tóm tắt cuộc hội thoại từ điểm đó trở đi]
[Các tin nhắn gốc được giữ lại trong transcript]
[Bản tóm tắt thay thế cuộc hội thoại hiển thị, giảm mức sử dụng context window]

User: Giờ hãy tiếp tục với cách tiếp cận đã hiệu quả.
```

## Những Điểm Chính

1. **Checkpoint là tự động**: Mỗi prompt của người dùng tạo một checkpoint -- không cần lưu thủ công
2. **Dùng Esc+Esc hoặc /rewind**: Đây là hai cách để mở trình duyệt checkpoint
3. **Chọn đúng tùy chọn khôi phục**: Khôi phục code, cuộc hội thoại, cả hai, hoặc tóm tắt tùy theo nhu cầu của bạn
4. **Đừng ngại thử nghiệm**: Checkpoint giúp bạn an toàn khi thử những thay đổi lớn
5. **Kết hợp với git**: Dùng checkpoint để khám phá, git cho công việc đã hoàn thiện
6. **Tóm tắt các phiên dài**: Dùng "Summarize from here" để giữ cuộc hội thoại dễ quản lý

---
**Cập Nhật Lần Cuối**: Ngày 29 tháng 7 năm 2026
**Phiên Bản Claude Code**: 2.1.220
**Nguồn**:
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/model-config
**Các Mô Hình Tương Thích**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
