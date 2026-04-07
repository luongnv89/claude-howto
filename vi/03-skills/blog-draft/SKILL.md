---
name: blog-draft
description: Soạn thảo bài đăng blog từ ý tưởng và tài nguyên. Sử dụng khi người dùng muốn viết bài blog, tạo nội dung từ nghiên cứu, hoặc soạn thảo bài viết. Hướng dẫn qua nghiên cứu, động não, lập dàn ý, và soạn thảo lặp lại với kiểm soát phiên bản.
---

## Đầu Vào Người Dùng

```text
$ARGUMENTS
```

Bạn **BẮT BUỘC** phải xem xét đầu vào của người dùng trước khi tiếp tục. Người dùng nên cung cấp:
- **Ý tưởng/Chủ đề**: Khái niệm hoặc chủ đề chính cho bài đăng blog
- **Tài nguyên**: URLs, files, hoặc tài liệu tham khảo để nghiên cứu (tùy chọn nhưng được khuyến nghị)
- **Đối tượng mục tiêu**: Bài đăng blog dành cho ai (tùy chọn)
- **Giọng điệu/Phong cách**: Trang trọng, thân mật, kỹ thuật, v.v. (tùy chọn)

**QUAN TRỌNG**: Nếu người dùng đang yêu cầu cập nhật cho một **bài đăng blog hiện có**, bỏ qua các bước 0-8 và bắt đầu trực tiếp tại **Bước 9**. Đọc các file draft hiện có trước, sau đó tiếp tục với quy trình lặp lại.

## Quy Trình Thực Thi

Làm theo các bước này tuần tự. **Đừng bỏ qua bước hoặc tiếp tục mà không có sự chấp thuận của người dùng nơi được chỉ ra.**

### Bước 0: Tạo Thư Mục Dự Án

1. Tạo tên thư mục sử dụng định dạng: `YYYY-MM-DD-ten-chu-de-ngan`
   - Sử dụng ngày hôm nay
   - Tạo một slug ngắn, thân thiện với URL từ chủ đề (chữ thường, gạch ngang, tối đa 5 từ)

2. Tạo cấu trúc thư mục:
   ```
   blog-posts/
   └── YYYY-MM-DD-ten-chu-de-ngan/
       └── resources/
   ```

3. Xác nhận việc tạo thư mục với người dùng trước khi tiếp tục.

### Bước 1: Nghiên Cứu & Thu Thập Tài Nguyên

1. Tạo thư mục con `resources/` trong thư mục bài đăng blog

2. Với mỗi tài nguyên được cung cấp:
   - **URLs**: Lấy và lưu thông tin chính vào `resources/` dưới dạng files markdown
   - **Files**: Đọc và tóm tắt trong `resources/`
   - **Chủ đề**: Sử dụng tìm kiếm web để thu thập thông tin cập nhật

3. Với mỗi tài nguyên, tạo một file tóm tắt trong `resources/`:
   - `resources/source-1-[ten-ngan].md`
   - `resources/source-2-[ten-ngan].md`
   - v.v.

4. Mỗi tóm tắt nên bao gồm:
   ```markdown
   # Nguồn: [Tiêu Đề/URL]

   ## Các Điểm Chính
   - Điểm 1
   - Điểm 2

   ## Trích Dẫn/Dữ Liệu Liên Quan
   - Trích dẫn hoặc thống kê 1
   - Trích dẫn hoặc thống kê 2

   ## Cái Này Liên Quan Đến Chủ Đề Như Thế Nào
   Giải thích ngắn về sự liên quan
   ```

5. Trình bày tóm tắt nghiên cứu cho người dùng.

### Bước 2: Động Não & Làm Rõ

1. Dựa trên ý tưởng và các tài nguyên đã nghiên cứu, trình bày:
   - **Chủ đề chính** được xác định từ nghiên cứu
   - **Góc độ tiềm năng** cho bài đăng blog
   - **Các điểm chính** nên được bao phủ
   - **Khoảng trống** trong thông tin cần làm rõ

2. Đặt các câu hỏi làm rõ:
   - Điều chính bạn muốn người đọc nhận được là gì?
   - Có điểm cụ thể nào từ nghiên cứu bạn muốn nhấn mạnh không?
   - Độ dài mục tiêu là bao nhiêu? (ngắn: 500-800 từ, trung bình: 1000-1500, dài: 2000+)
   - Có điểm nào bạn muốn loại bỏ không?

3. **Chờ phản hồi của người dùng trước khi tiếp tục.**

### Bước 3: Đề Xuất Dàn Ý

1. Tạo một dàn ý có cấu trúc bao gồm:

   ```markdown
   # Dàn Ý Bài Đăng Blog: [Tiêu Đề]

   ## Thông Tin Meta
   - **Đối Tượng Mục Tiêu**: [ai]
   - **Giọng Điệu**: [phong cách]
   - **Độ Dài Mục Tiêu**: [số lượng từ]
   - **Điểm Chính Lấy Được**: [thông điệp chính]

   ## Cấu Trúc Được Đề Xuất

   ### Mở Bài/Giới Thiệu
   - Ý tưởng mở bài hấp dẫn
   - Thiết lập bối cảnh
   - Tuyên bố luận điểm

   ### Phần 1: [Tiêu Đề]
   - Điểm chính A
   - Điểm chính B
   - Bằng chứng hỗ trợ từ [nguồn]

   ### Phần 2: [Tiêu Đề]
   - Điểm chính A
   - Điểm chính B

   [Tiếp tục cho tất cả các phần...]

   ### Kết Luận
   - Tóm tắt các điểm chính
   - Kêu gọi hành động hoặc suy nghĩ cuối cùng

   ## Nguồn Để Trích Dẫn
   - Nguồn 1
   - Nguồn 2
   ```

2. Trình bày dàn ý cho người dùng và **yêu cầu chấp thuận hoặc chỉnh sửa**.

### Bước 4: Lưu Dàn Ý Được Chấp Thuận

1. Khi người dùng chấp thuận dàn ý, lưu nó vào `OUTLINE.md` trong thư mục bài đăng blog.

2. Xác nhận dàn ý đã được lưu.

### Bước 5: Commit Dàn Ý (nếu trong git repo)

1. Kiểm tra xem thư mục hiện tại có phải là một git repository không.

2. Nếu có:
   - Stage các file mới: thư mục bài đăng blog, resources, và OUTLINE.md
   - Tạo commit với thông điệp: `docs: Add outline for blog post - [ten-chu-de]`
   - Push đến remote

3. Nếu không phải là git repo, bỏ qua bước này và thông báo cho người dùng.

### Bước 6: Viết Bản Nháp

1. Dựa trên dàn ý được chấp thuận, viết bản nháp bài đăng blog đầy đủ.

2. Làm theo cấu trúc từ OUTLINE.md chính xác.

3. Bao gồm:
   - Giới thiệu hấp dẫn với mở bài
   - Các tiêu đề phần rõ ràng
   - Bằng chứng hỗ trợ và ví dụ từ nghiên cứu
   - Chuyển tiếp mượt mà giữa các phần
   - Kết luận mạnh mẽ với điểm chính
   - **Trích dẫn**: Tất cả các so sánh, thống kê, dữ liệu, và yêu cầu thực tế PHẢI trích dẫn nguồn gốc

4. Lưu bản nháp dưới dạng `draft-v0.1.md` trong thư mục bài đăng blog.

5. Định dạng:
   ```markdown
   # [Tiêu Đề Bài Đăng Blog]

   *[Tùy chọn: phụ đề hoặc câu khẩu hiệu]*

   [Nội dung đầy đủ với các trích dẫn nội tuyến...]

   ---

   ## Tài Liệu Tham Khảo
   - [1] Tiêu Đề Nguồn 1 - URL hoặc Trích Dẫn
   - [2] Tiêu Đề Nguồn 2 - URL hoặc Trích Dẫn
   - [3] Tiêu Đề Nguồn 3 - URL hoặc Trích Dẫn
   ```

6. **Yêu Cầu Trích Dẫn**:
   - Mọi điểm dữ liệu, thống kê, hoặc so sánh PHẢI có trích dẫn nội tuyến
   - Sử dụng tài liệu tham khảo đánh số [1], [2], v.v., hoặc trích dẫn có tên [Tên Nguồn]
   - Liên kết các trích dẫn với phần Tài Liệu Tham Khảo ở cuối
   - Ví dụ: "Các nghiên cứu cho thấy 65% nhà phát triển ưa thích TypeScript [1]"
   - Ví dụ: "React hoạt động tốt hơn Vue 20% về tốc độ render [React Benchmarks 2024]"

### Bước 7: Commit Bản Nháp (nếu trong git repo)

1. Kiểm tra xem có trong git repository không.

2. Nếu có:
   - Stage file bản nháp
   - Tạo commit với thông điệp: `docs: Add draft v0.1 for blog post - [ten-chu-de]`
   - Push đến remote

3. Nếu không phải là git repo, bỏ qua và thông báo cho người dùng.

### Bước 8: Trình Bày Bản Nháp Để Xem Xét

1. Trình bày nội dung bản nháp cho người dùng.

2. Yêu cầu phản hồi:
   - Ấn tượng tổng thể?
   - Các phần cần mở rộng hoặc giảm bớt?
   - Cần điều chỉnh giọng điệu?
   - Thiếu thông tin?
   - Chỉnh sửa hoặc viết lại cụ thể?

3. **Chờ phản hồi của người dùng.**

### Bước 9: Lặp Lại Hoặc Hoàn Thành

**Nếu người dùng yêu cầu thay đổi:**
1. Ghi chú tất cả các chỉnh sửa được yêu cầu
2. Quay lại Bước 6 với các điều chỉnh sau:
   - Tăng số phiên bản (v0.2, v0.3, v.v.)
   - Kết hợp tất cả phản hồi
   - Lưu dưới dạng `draft-v[X.Y].md`
   - Lặp lại Các bước 7-8

**Nếu người dùng chấp thuận:**
1. Xác nhận phiên bản bản nháp cuối cùng
2. Tùy chọn đổi tên thành `final.md` nếu người dùng yêu cầu
3. Tóm tắt quy trình tạo bài đăng blog:
   - Tổng số phiên bản được tạo
   - Các thay đổi chính giữa các phiên bản
   - Số lượng từ cuối cùng
   - Các file được tạo

## Theo Dõi Phiên Bản

Tất cả bản nháp được bảo tồn với việc đánh số phiên bản tăng dần:
- `draft-v0.1.md` - Bản nháp ban đầu
- `draft-v0.2.md` - Sau vòng phản hồi đầu tiên
- `draft-v0.3.md` - Sau vòng phản hồi thứ hai
- v.v.

Điều này cho phép theo dõi sự phát triển của bài đăng blog và hoàn tác nếu cần.

## Cấu Trúc File Đầu Ra

```
blog-posts/
└── YYYY-MM-DD-ten-chu-de/
    ├── resources/
    │   ├── source-1-name.md
    │   ├── source-2-name.md
    │   └── ...
    ├── OUTLINE.md
    ├── draft-v0.1.md
    ├── draft-v0.2.md (nếu có lặp lại)
    └── draft-v0.3.md (nếu có nhiều lặp lại hơn)
```

## Mẹo Để Chất Lượng

- **Mở bài**: Bắt đầu với một câu hỏi, sự thật đáng ngạc nhiên, hoặc kịch bản có thể liên quan
- **Dòng Chảy**: Mỗi đoạn nên kết nối với đoạn tiếp theo
- **Bằng Chứng**: Hỗ trợ các yêu cầu với dữ liệu từ nghiên cứu
- **Trích Dẫn**: LUÔN LUÔN trích dẫn nguồn cho:
  - Tất cả thống kê và điểm dữ liệu (ví dụ: "Theo [Nguồn], 75% của...")
  - So sánh giữa các sản phẩm, dịch vụ, hoặc cách tiếp cận (ví dụ: "X hoạt động nhanh hơn gấp 2 lần so với Y [Nguồn]")
  - Các yêu cầu thực tế về xu hướng thị trường, phát hiện nghiên cứu, hoặc điểm chuẩn
  - Sử dụng trích dẫn nội tuyến với định dạng: [Tên Nguồn] hoặc [Tác Giả, Năm]
- **Giọng**: Duy trì giọng điệu nhất quán throughout
- **Độ Dài**: Tôn trọng số lượng từ mục tiêu
- **Khả Đọc**: Sử dụng các đoạn ngắn, gạch đầu dòng nơi phù hợp
- **CTA**: Kết thúc với một lời kêu gọi hành động rõ ràng hoặc câu hỏi đáng suy ngẫm

## Ghi Chú

- Luôn chờ chấp thuận của người dùng tại các điểm kiểm tra được phác thảo
- Bảo tồn tất cả các phiên bản bản nháp để lịch sử
- Sử dụng tìm kiếm web để có thông tin cập nhật khi URLs được cung cấp
- Nếu tài nguyên không đủ, yêu cầu người dùng thêm hoặc đề xuất nghiên cứu bổ sung
- Thích ứng giọng điệu dựa trên đối tượng mục tiêu (kỹ thuật, chung, kinh doanh, v.v.)
