# Ví Dụ Về Chế Độ Lập Kế Hoạch

Các ví dụ thực tế minh họa cách sử dụng hiệu quả chế độ lập kế hoạch (planning mode) trong Claude Code.

## Ví Dụ 1: Xây Dựng REST API

### Không Dùng Chế Độ Lập Kế Hoạch

```
User: Xây dựng một REST API cho blog

Claude: Tôi sẽ tạo API...
[Bắt đầu viết code ngay lập tức, có thể bỏ sót yêu cầu]
```

### Dùng Chế Độ Lập Kế Hoạch

```
User: /plan Xây dựng một REST API cho blog

Claude: Để tôi tạo một kế hoạch toàn diện cho blog API.

## Kế Hoạch Triển Khai Blog REST API

### Giai đoạn 1: Thiết lập dự án (15 phút)
1. Khởi tạo dự án Node.js với Express
2. Thiết lập cấu hình TypeScript
3. Cài đặt dependencies (express, pg, jwt, joi)
4. Cấu hình biến môi trường
5. Thiết lập cấu trúc dự án

### Giai đoạn 2: Tầng cơ sở dữ liệu (30 phút)
6. Thiết kế schema cơ sở dữ liệu
   - bảng users (id, email, password_hash, created_at)
   - bảng posts (id, user_id, title, content, published, created_at, updated_at)
   - bảng comments (id, post_id, user_id, content, created_at)
7. Tạo các file migration
8. Thiết lập connection pool cho cơ sở dữ liệu
9. Triển khai các model cơ sở dữ liệu

### Giai đoạn 3: Xác thực (45 phút)
10. Triển khai endpoint đăng ký người dùng
11. Triển khai endpoint đăng nhập với JWT
12. Tạo middleware xác thực
13. Thêm băm mật khẩu bằng bcrypt
14. Triển khai logic làm mới token

### Giai đoạn 4: Posts API (40 phút)
15. GET /api/posts - Liệt kê tất cả bài viết đã xuất bản (có phân trang)
16. GET /api/posts/:id - Lấy một bài viết
17. POST /api/posts - Tạo bài viết mới (yêu cầu xác thực)
18. PUT /api/posts/:id - Cập nhật bài viết (yêu cầu xác thực, kiểm tra quyền sở hữu)
19. DELETE /api/posts/:id - Xóa bài viết (yêu cầu xác thực, kiểm tra quyền sở hữu)
20. GET /api/users/:id/posts - Lấy các bài viết của người dùng

### Giai đoạn 5: Comments API (30 phút)
21. GET /api/posts/:id/comments - Lấy bình luận của bài viết
22. POST /api/posts/:id/comments - Thêm bình luận (yêu cầu xác thực)
23. DELETE /api/comments/:id - Xóa bình luận (yêu cầu xác thực, kiểm tra quyền sở hữu)

### Giai đoạn 6: Validation & xử lý lỗi (30 phút)
24. Thêm validation cho request bằng Joi
25. Triển khai trình xử lý lỗi toàn cục
26. Thêm làm sạch (sanitization) dữ liệu đầu vào
27. Triển khai giới hạn tần suất (rate limiting)

### Giai đoạn 7: Kiểm thử (60 phút)
28. Viết unit test cho các model
29. Viết integration test cho các endpoint xác thực
30. Viết integration test cho các endpoint posts
31. Viết integration test cho các endpoint comments
32. Đạt độ bao phủ code từ 80% trở lên

### Giai đoạn 8: Tài liệu & triển khai (30 phút)
33. Tạo tài liệu API bằng Swagger
34. Tạo README kèm hướng dẫn thiết lập
35. Thêm cấu hình Docker
36. Thiết lập pipeline CI/CD

**Thời gian ước tính**: 4,5 giờ
**Số file cần tạo**: ~25
**Công nghệ chính**: Express, PostgreSQL, JWT, TypeScript

**Tóm tắt các API endpoint**:
- Xác thực: 2 endpoint
- Posts: 6 endpoint
- Comments: 3 endpoint
- Tổng cộng: 11 endpoint

Sẵn sàng tiến hành? (yes/no/modify)

User: yes

Claude: Bắt đầu Giai đoạn 1: Thiết lập dự án...
[Triển khai từng giai đoạn một cách có hệ thống]
```

## Ví Dụ 2: Di Chuyển Cơ Sở Dữ Liệu

### Dùng Chế Độ Lập Kế Hoạch

```
User: /plan Di chuyển từ MongoDB sang PostgreSQL

Claude: Đây là một cuộc di chuyển phức tạp. Để tôi tạo một kế hoạch chi tiết.

## Kế Hoạch Di Chuyển Từ MongoDB Sang PostgreSQL

### Giai đoạn 1: Phân tích & chuẩn bị (Ngày 1)
1. Phân tích schema MongoDB hiện tại
2. Xác định các mối quan hệ và ràng buộc dữ liệu
3. Ghi lại khối lượng dữ liệu hiện tại và tốc độ tăng trưởng
4. Thiết kế schema PostgreSQL tương đương
5. Lên kế hoạch ánh xạ kiểu dữ liệu
6. Xác định các thách thức tiềm ẩn khi di chuyển

### Giai đoạn 2: Thiết lập PostgreSQL (Ngày 1)
7. Thiết lập cơ sở dữ liệu PostgreSQL
8. Tạo schema với các bảng, index, ràng buộc
9. Thiết lập connection pooling
10. Cấu hình chiến lược sao lưu

### Giai đoạn 3: Triển khai ghi kép (Ngày 2-3)
11. Tạo tầng trừu tượng cho cơ sở dữ liệu
12. Triển khai ghi kép vào cả hai cơ sở dữ liệu
13. Thêm kiểm tra tính nhất quán dữ liệu
14. Triển khai ghi kép lên staging
15. Giám sát các vấn đề phát sinh

### Giai đoạn 4: Di chuyển dữ liệu (Ngày 4)
16. Tạo script xuất dữ liệu cho MongoDB
17. Tạo script nhập dữ liệu cho PostgreSQL
18. Triển khai logic chuyển đổi dữ liệu
19. Chạy di chuyển lần đầu trên bản sao dữ liệu production
20. Xác minh tính toàn vẹn của dữ liệu đã di chuyển

### Giai đoạn 5: Chuyển đổi dần dần (Ngày 5-7)
21. Bật ghi kép trên production
22. Di chuyển dữ liệu lịch sử theo từng lô
23. Liên tục xác minh tính nhất quán dữ liệu
24. Giám sát cả hai cơ sở dữ liệu
25. Sửa mọi vấn đề đồng bộ dữ liệu

### Giai đoạn 6: PostgreSQL làm chính (Ngày 8)
26. Chuyển các thao tác đọc sang PostgreSQL
27. Giám sát hiệu năng truy vấn
28. Tối ưu các truy vấn chậm
29. Tiếp tục ghi kép để đảm bảo an toàn

### Giai đoạn 7: Ngừng sử dụng MongoDB (Ngày 9-10)
30. Dừng ghi vào MongoDB
31. Giữ MongoDB làm bản sao lưu trong 2 tuần
32. Gỡ các dependency MongoDB khỏi code
33. Lưu trữ dữ liệu MongoDB
34. Ngừng hoạt động instance MongoDB

**Thời gian ước tính**: 10 ngày
**Mức độ rủi ro**: Cao
**Chiến lược rollback**: Giữ MongoDB chạy cùng với ghi kép
**Tiêu chí thành công**:
- Không mất dữ liệu
- Hiệu năng suy giảm <5%
- Tất cả test đều pass

**Rủi ro chính**:
1. Dữ liệu không nhất quán trong quá trình di chuyển
2. Suy giảm hiệu năng truy vấn
3. Ứng dụng bị gián đoạn
4. Mất dữ liệu

**Biện pháp giảm thiểu**:
- Mẫu ghi kép để đảm bảo an toàn
- Chuyển đổi dần dần
- Giám sát liên tục
- Khả năng rollback nhanh

Tiến hành theo kế hoạch này? (yes/no/modify)

User: Modify - hãy thêm kế hoạch rollback cho từng giai đoạn

Claude: Đã cập nhật kế hoạch với quy trình rollback cho từng giai đoạn...
```

## Ví Dụ 3: Refactor Frontend

```
User: /plan Refactor ứng dụng React của chúng ta từ class component sang hooks

Claude: Tôi sẽ tạo một kế hoạch refactor có hệ thống.

## Kế Hoạch Chuyển React Từ Class Sang Hooks

### Giai đoạn 1: Chuẩn bị & phân tích (2 giờ)
1. Rà soát tất cả class component (tìm tất cả file .jsx/.tsx)
2. Phân loại theo độ phức tạp:
   - Đơn giản (chỉ có state): ~15 component
   - Trung bình (có lifecycle method): ~23 component
   - Phức tạp (nhiều lifecycle, refs): ~8 component
3. Xác định các thư viện bên thứ ba cần cập nhật
4. Tạo đồ thị phụ thuộc giữa các component
5. Lên kế hoạch thứ tự chuyển đổi (node lá trước)

### Giai đoạn 2: Thiết lập & công cụ (1 giờ)
6. Cập nhật React lên v18+
7. Thiết lập quy tắc ESLint cho hooks
8. Tạo các template chuyển đổi
9. Thiết lập test tự động
10. Tạo checkpoint trước khi bắt đầu

### Giai đoạn 3: Chuyển các component đơn giản (4 giờ)
11. Chuyển đổi các component có state đơn giản (15 component)
12. Thay this.state bằng useState
13. Thay this.setState bằng các hàm setter của state
14. Kiểm thử từng component sau khi chuyển đổi
15. Cập nhật test

### Giai đoạn 4: Chuyển các component trung bình (8 giờ)
16. Chuyển đổi các component có lifecycle method (23 component)
17. Thay componentDidMount bằng useEffect
18. Thay componentDidUpdate bằng useEffect
19. Thay componentWillUnmount bằng phần cleanup của useEffect
20. Kiểm thử kỹ lưỡng

### Giai đoạn 5: Chuyển các component phức tạp (12 giờ)
21. Chuyển đổi các component phức tạp (8 component)
22. Thay refs bằng useRef
23. Tách custom hook cho logic dùng chung
24. Xử lý các trường hợp biên (nhiều useEffect)
25. Kiểm thử toàn diện

### Giai đoạn 6: Tách logic dùng chung (6 giờ)
26. Xác định logic trùng lặp giữa các component
27. Tạo custom hook:
    - useAuth
    - useFetch
    - useLocalStorage
    - useDebounce
28. Refactor các component để dùng custom hook
29. Kiểm thử custom hook một cách độc lập

### Giai đoạn 7: Tối ưu hiệu năng (4 giờ)
30. Thêm React.memo ở những chỗ cần thiết
31. Tối ưu bằng useCallback
32. Tối ưu bằng useMemo
33. Profile và sửa các suy giảm hiệu năng

### Giai đoạn 8: Dọn dẹp & tài liệu (2 giờ)
34. Gỡ các tiện ích class component không còn dùng
35. Cập nhật tài liệu
36. Cập nhật hướng dẫn viết code
37. Tạo hướng dẫn chuyển đổi cho team

**Thời gian ước tính**: 5 ngày (39 giờ)
**Số file cần sửa**: 46 component
**Mức độ rủi ro**: Trung bình

**Thứ tự chuyển đổi**:
1. Component lá (không có phụ thuộc)
2. Component tầng giữa
3. Container component tầng trên cùng
4. App.jsx (cuối cùng)

**Chiến lược kiểm thử**:
- Unit test cho từng component
- Integration test cho các luồng người dùng
- Visual regression test
- Benchmark hiệu năng

**Chỉ số thành công**:
- Tất cả test đều pass
- Không có lỗi hồi quy về giao diện
- Hiệu năng được giữ nguyên hoặc cải thiện
- Kích thước bundle không tăng đáng kể

Tiến hành? (yes/no/modify)
```

## Ví Dụ 4: Triển Khai Bảo Mật

```
User: /plan Triển khai bảo mật toàn diện cho ứng dụng web của chúng ta

Claude: Để tôi tạo một kế hoạch triển khai bảo mật kỹ lưỡng.

## Kế Hoạch Triển Khai Bảo Mật Ứng Dụng Web

### Giai đoạn 1: Kiểm toán bảo mật (Ngày 1)
1. Chạy các công cụ quét bảo mật tự động (npm audit, Snyk)
2. Rà soát dependencies để tìm lỗ hổng
3. Kiểm tra tuân thủ OWASP Top 10
4. Kiểm toán các luồng xác thực
5. Rà soát cách xử lý dữ liệu
6. Ghi lại các lỗ hổng bảo mật hiện tại

### Giai đoạn 2: Tăng cường xác thực (Ngày 2-3)
7. Áp dụng yêu cầu mật khẩu mạnh
8. Thêm thước đo độ mạnh mật khẩu
9. Áp dụng rate limiting cho đăng nhập
10. Khóa tài khoản sau nhiều lần đăng nhập thất bại
11. Triển khai 2FA (TOTP)
12. Cải thiện quản lý phiên
13. Triển khai luồng đặt lại mật khẩu an toàn

### Giai đoạn 3: Phân quyền & kiểm soát truy cập (Ngày 3-4)
14. Triển khai RBAC (Role-Based Access Control)
15. Thêm kiểm tra quyền trên tất cả endpoint
16. Áp dụng nguyên tắc đặc quyền tối thiểu
17. Thêm ghi log kiểm toán cho các thao tác nhạy cảm
18. Triển khai phân quyền ở cấp tài nguyên

### Giai đoạn 4: Bảo vệ dữ liệu (Ngày 4-5)
19. Mã hóa dữ liệu lưu trữ (các trường nhạy cảm)
20. Đảm bảo TLS/SSL cho mọi kết nối
21. Triển khai lưu trữ phiên an toàn
22. Che dữ liệu PII trong log
23. Áp dụng chính sách lưu giữ dữ liệu
24. Xử lý upload file an toàn

### Giai đoạn 5: Validation & làm sạch đầu vào (Ngày 5-6)
25. Validate đầu vào trên tất cả endpoint
26. Thêm bảo vệ XSS (Content Security Policy)
27. Ngăn chặn SQL injection (truy vấn tham số hóa)
28. Thêm bảo vệ CSRF
29. Giới hạn kích thước request
30. Validate loại file khi upload

### Giai đoạn 6: Security header & cấu hình (Ngày 6)
31. Thêm các security header:
    - Strict-Transport-Security
    - X-Content-Type-Options
    - X-Frame-Options
    - X-XSS-Protection
    - Content-Security-Policy
32. Cấu hình CORS đúng cách
33. Tắt các HTTP method không cần thiết
34. Gỡ các header tiết lộ phiên bản server

### Giai đoạn 7: Giám sát & ghi log (Ngày 7)
35. Ghi log các sự kiện bảo mật
36. Thêm phát hiện bất thường
37. Thiết lập phát hiện xâm nhập
38. Triển khai cảnh báo thời gian thực
39. Tạo dashboard bảo mật

### Giai đoạn 8: Kiểm thử & tài liệu (Ngày 8-9)
40. Thực hiện kiểm thử xâm nhập (penetration testing)
41. Chạy các công cụ quét bảo mật
42. Kiểm thử tất cả tính năng bảo mật
43. Tạo tài liệu bảo mật
44. Đào tạo team về các thực hành bảo mật
45. Tạo kế hoạch ứng phó sự cố

### Giai đoạn 9: Tuân thủ & chính sách (Ngày 10)
46. Kiểm tra tuân thủ GDPR
47. Tạo chính sách quyền riêng tư
48. Triển khai các quyền của chủ thể dữ liệu
49. Thêm yêu cầu đồng ý cookie
50. Tạo tài liệu chính sách bảo mật

**Thời gian ước tính**: 10 ngày
**Mức độ rủi ro**: Nghiêm trọng
**Độ ưu tiên**: Cao

**Tóm tắt các cải tiến bảo mật**:
- Xác thực: 7 cải tiến
- Phân quyền: 5 cải tiến
- Bảo vệ dữ liệu: 6 cải tiến
- Validation đầu vào: 6 cải tiến
- Hạ tầng: 9 cải tiến
- Giám sát: 5 cải tiến

**Tuân thủ**: OWASP Top 10, GDPR

**Tiêu chí thành công**:
- Không có lỗ hổng nghiêm trọng
- Đã giảm thiểu toàn bộ OWASP Top 10
- Điểm bảo mật >90/100
- Đã xử lý mọi vấn đề từ pen test

Tiến hành? (yes/no/modify)
```

## Ví Dụ 5: Tối Ưu Hiệu Năng

```
User: /plan Tối ưu website thương mại điện tử đang chạy chậm của chúng ta

Claude: Để tôi tạo một kế hoạch tối ưu hiệu năng toàn diện.

## Kế Hoạch Tối Ưu Hiệu Năng Thương Mại Điện Tử

### Giai đoạn 1: Kiểm toán hiệu năng (4 giờ)
1. Chạy kiểm toán Lighthouse
2. Phân tích performance profile trong Chrome DevTools
3. Đo các chỉ số Core Web Vitals:
   - LCP (Largest Contentful Paint)
   - FID (First Input Delay)
   - CLS (Cumulative Layout Shift)
4. Xác định các điểm nghẽn hiệu năng
5. Tạo bộ chỉ số hiệu năng nền (baseline)

**Chỉ số hiện tại**:
- LCP: 4.2s (mục tiêu: <2.5s)
- FID: 280ms (mục tiêu: <100ms)
- CLS: 0.25 (mục tiêu: <0.1)
- Thời gian tải trang: 8.3s (mục tiêu: <3s)

### Giai đoạn 2: Tối ưu hình ảnh (6 giờ)
6. Chuyển hình ảnh sang định dạng WebP
7. Triển khai responsive image
8. Thêm lazy loading cho hình ảnh
9. Tối ưu kích thước hình ảnh (nén)
10. Dùng CDN cho hình ảnh
11. Thêm placeholder cho hình ảnh

**Tác động dự kiến**: -40% thời gian tải

### Giai đoạn 3: Code splitting & lazy loading (8 giờ)
12. Triển khai code splitting theo route
13. Lazy load các component không quan trọng
14. Tách các vendor bundle
15. Tối ưu kích thước chunk
16. Triển khai dynamic import
17. Thêm preload cho các tài nguyên quan trọng

**Tác động dự kiến**: -30% kích thước bundle ban đầu

### Giai đoạn 4: Chiến lược caching (6 giờ)
18. Triển khai browser caching (Cache-Control)
19. Thêm service worker để hỗ trợ offline
20. Cache response của API
21. Thêm Redis cache cho truy vấn cơ sở dữ liệu
22. Triển khai stale-while-revalidate
23. Cấu hình caching trên CDN

**Tác động dự kiến**: -50% thời gian phản hồi API

### Giai đoạn 5: Tối ưu cơ sở dữ liệu (8 giờ)
24. Thêm index cho cơ sở dữ liệu
25. Tối ưu các truy vấn chậm (>100ms)
26. Cache kết quả truy vấn
27. Thêm connection pooling
28. Phi chuẩn hóa (denormalize) ở những chỗ phù hợp
29. Triển khai read replica cho cơ sở dữ liệu

**Tác động dự kiến**: -60% thời gian truy vấn cơ sở dữ liệu

### Giai đoạn 6: Tối ưu frontend (10 giờ)
30. Minify và nén JavaScript
31. Minify và nén CSS
32. Gỡ CSS không dùng đến (PurgeCSS)
33. Triển khai critical CSS
34. Trì hoãn JavaScript không quan trọng
35. Giảm kích thước DOM
36. Tối ưu việc render React (memo, useMemo)
37. Triển khai virtual scrolling cho danh sách dài

**Tác động dự kiến**: -35% thời gian thực thi JavaScript

### Giai đoạn 7: Tối ưu mạng (4 giờ)
38. Bật HTTP/2
39. Thêm resource hint (preconnect, prefetch)
40. Giảm số lượng HTTP request
41. Bật nén Brotli
42. Tối ưu các script bên thứ ba

**Tác động dự kiến**: -25% thời gian mạng

### Giai đoạn 8: Giám sát & kiểm thử (4 giờ)
43. Thiết lập giám sát hiệu năng (Datadog/New Relic)
44. Thêm Real User Monitoring (RUM)
45. Tạo ngân sách hiệu năng (performance budget)
46. Thiết lập Lighthouse CI tự động
47. Kiểm thử trên thiết bị thật

**Thời gian ước tính**: 50 giờ (2 tuần)

**Chỉ số mục tiêu** (bách phân vị thứ 90):
- LCP: <2.0s (từ 4.2s) ✅
- FID: <50ms (từ 280ms) ✅
- CLS: <0.05 (từ 0.25) ✅
- Thời gian tải trang: <2.5s (từ 8.3s) ✅

**Tác động dự kiến đến doanh thu**:
- Nhanh hơn 100ms = tăng 1% tỷ lệ chuyển đổi
- Mục tiêu: cải thiện 5.8s = tăng ~58% tỷ lệ chuyển đổi
- Doanh thu tăng thêm ước tính: Đáng kể

**Thứ tự ưu tiên**:
1. Tối ưu hình ảnh (thắng nhanh)
2. Code splitting (tác động cao)
3. Caching (tác động cao)
4. Tối ưu cơ sở dữ liệu (quan trọng)
5. Tối ưu frontend (hoàn thiện)

Tiến hành theo kế hoạch này? (yes/no/modify)
```

## Những Điểm Chính

### Lợi Ích Của Chế Độ Lập Kế Hoạch

1. **Rõ ràng**: Có lộ trình rõ ràng trước khi bắt đầu
2. **Ước lượng**: Ước tính thời gian và công sức
3. **Đánh giá rủi ro**: Phát hiện sớm các vấn đề tiềm ẩn
4. **Ưu tiên**: Sắp xếp công việc theo thứ tự hợp lý
5. **Phê duyệt**: Xem xét và phê duyệt trước khi thực thi
6. **Điều chỉnh**: Điều chỉnh kế hoạch dựa trên phản hồi

### Khi Nào Nên Dùng Chế Độ Lập Kế Hoạch

✅ **Luôn dùng cho**:
- Dự án kéo dài nhiều ngày
- Cộng tác trong team
- Thay đổi hệ thống quan trọng
- Học các khái niệm mới
- Refactor phức tạp

❌ **Không nên dùng cho**:
- Sửa lỗi
- Chỉnh sửa nhỏ
- Câu hỏi đơn giản
- Thử nghiệm nhanh

### Thực Hành Tốt Nhất

1. **Xem xét kế hoạch cẩn thận** trước khi phê duyệt
2. **Điều chỉnh kế hoạch** khi bạn phát hiện vấn đề
3. **Chia nhỏ** các tác vụ phức tạp
4. **Ước lượng thực tế** khung thời gian
5. **Bao gồm chiến lược rollback**
6. **Thêm tiêu chí** thành công
7. **Lên kế hoạch kiểm thử** ở mỗi giai đoạn

---
**Cập Nhật Lần Cuối**: Ngày 1 tháng 11 năm 2026
**Phiên Bản Claude Code**: 2.1.316
**Nguồn**:
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode
- https://code.claude.com/docs/en/model-config
**Các Mô Hình Tương Thích**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
