---
name: code-refactor
description: Refactor code có hệ thống dựa trên phương pháp luận của Martin Fowler. Sử dụng khi người dùng yêu cầu refactor code, cải thiện cấu trúc code, giảm nợ kỹ thuật, dọn code legacy, loại bỏ code smells, hoặc cải thiện khả năng duy trì code. Skill này hướng dẫn qua cách tiếp theo từng giai đoạn với nghiên cứu, lập kế hoạch, và triển khai tăng dần an toàn.
---

# Code Refactoring Skill

Một cách tiếp có hệ thống để refactor code dựa trên *Refactoring: Improving the Design of Existing Code* (ấn bản 2) của Martin Fowler. Skill này nhấn mạnh các thay đổi tăng dần, an toàn được hỗ trợ bởi tests.

> "Refactoring là quá trình thay đổi một hệ thống phần mềm theo cách mà nó không làm thay đổi hành vi bên ngoài của code nhưng cải thiện cấu trúc nội bộ của nó." — Martin Fowler

## Nguyên Tắc Cốt Lõi

1. **Bảo Tồn Hành Vi**: Hành vi bên ngoài phải không thay đổi
2. **Các Bước Nhỏ**: Thực hiện các thay đổi nhỏ, có thể test
3. **Được Dẫn Bởi Test**: Tests là lưới an toàn
4. **Liên Tục**: Refactoring là liên tục, không phải sự kiện một lần
5. **Hợp Tác**: Cần sự chấp thuận của người dùng tại mỗi giai đoạn

## Tổng Quan Workflow

```
Giai Đoạn 1: Nghiên Cứu & Phân Tích
    ↓
Giai Đoạn 2: Đánh Giá Phủ Vùng Test
    ↓
Giai Đoạn 3: Xác Định Code Smell
    ↓
Giai Đoạn 4: Tạo Kế Hoạch Refactoring
    ↓
Giai Đoạn 5: Triển Khai Tăng Dần
    ↓
Giai Đoạn 6: Review & Lặp Lại
```

---

## Giai Đoạn 1: Nghiên Cứu & Phân Tích

### Mục Tiêu
- Hiểu cấu trúc và mục đích của codebase
- Xác định phạm vi của refactoring
- Thu thập bối cảnh về các yêu cầu kinh doanh

### Câu Hỏi Đặt Cho Người Dùng
Trước khi bắt đầu, làm rõ:

1. **Phạm Vi**: Những file/module/hàm nào cần refactor?
2. **Mục Tiêu**: Bạn đang cố gắng giải quyết vấn đề gì? (khả đọc, hiệu suất, khả năng duy trì)
3. **Ràng Buộc**: Có những khu vực nào KHÔNG NÊN thay đổi không?
4. **Áp Lực Thời Gian**: Điều này có chặn công việc khác không?
5. **Trạng Thái Test**: Tests có tồn tại không? Chúng có pass không?

### Hành Động
- [ ] Đọc và hiểu code mục tiêu
- [ ] Xác định dependencies và integrations
- [ ] Tài liệu hóa kiến trúc hiện tại
- [ ] Ghi chú bất kỳ markers nợ kỹ thuật hiện có (TODOs, FIXMEs)

### Đầu Ra
Trình bày phát hiện cho người dùng:
- Tóm tắt cấu trúc code
- Các khu vực vấn đề được xác định
- Khuyến nghị ban đầu
- **Yêu cầu chấp thuận để tiếp tục**

---

## Giai Đoạn 2: Đánh Giá Phủ Vùng Test

### Tại Sao Tests Quan Trọng
> "Refactoring mà không có tests giống như lái xe mà không có thắt dây an toàn." — Martin Fowler

Tests là **bật dụng chính** của refactoring an toàn. Không có chúng, bạn có nguy cơ giới thiệu bugs.

### Các Bước Đánh Giá

1. **Kiểm tra các test hiện có**
   ```bash
   # Tìm các file test
   find . -name "*test*" -o -name "*spec*" | head -20
   ```

2. **Chạy các test hiện có**
   ```bash
   # JavaScript/TypeScript
   npm test

   # Python
   pytest -v

   # Java
   mvn test
   ```

3. **Kiểm tra phủ vùng (nếu có)**
   ```bash
   # JavaScript
   npm run test:coverage

   # Python
   pytest --cov=.
   ```

### Điểm Quyết Định: Hỏi Người Dùng

**Nếu tests tồn tại và pass:**
- Tiếp tục đến Giai Đoạn 3

**Nếu tests bị thiếu hoặc không hoàn chỉnh:**
Trình bày các tùy chọn:
1. Viết tests trước (khuyến nghị)
2. Thêm tests tăng dần trong khi refactoring
3. Tiếp tục mà không có tests (rủi ro - yêu cầu sự thừa nhận của người dùng)

**Nếu tests đang fail:**
- DỪNG LẠI. Sửa các test fail trước khi refactoring
- Hỏi người dùng: Chúng ta nên sửa tests trước không?

### Hướng Dẫn Viết Test (nếu cần)

Đối với mỗi hàm được refactor, đảm bảo tests bao phủ:
- Happy path (hoạt động bình thường)
- Các trường hợp ngoại lệ (đầu vào trống, null, ranh giới)
- Các kịch bản lỗi (đầu vào không hợp lệ, ngoại lệ)

Sử dụng chu trình "red-green-refactor":
1. Viết test fail (red)
2. Làm cho nó pass (green)
3. Refactor

---

## Giai Đoạn 3: Xác Định Code Smell

### Code Smells Là Gì?
Các triệu chứng của các vấn đề sâu hơn trong code. Chúng không phải là bugs, nhưng là các chỉ báo rằng code có thể được cải thiện.

### Các Code Smells Phổ Biến Để Kiểm Tra

Xem [references/code-smells.md](../../../03-skills/refactor/references/code-smells.md) để có danh sách đầy đủ.

#### Tham Khảo Nhanh

| Smell | Dấu Hiệu | Tác Động |
|-------|-------|--------|
| **Long Method** | Methods > 30-50 dòng | Khó hiểu, test, duy trì |
| **Duplicated Code** | Cùng logic ở nhiều nơi | Cần sửa lỗi ở nhiều nơi |
| **Large Class** | Class với quá nhiều trách nhiệm | Vi phạm Single Responsibility |
| **Feature Envy** | Method sử dụng dữ liệu class khác nhiều | Đóng gói kém |
| **Primitive Obsession** | Lạm dụng primitives thay vì objects | Thiếu các khái niệm domain |
| **Long Parameter List** | Methods với 4+ parameters | Khó gọi đúng |
| **Data Clumps** | Cùng dữ liệu xuất hiện cùng nhau | Thiếu abstraction |
| **Switch Statements** | Switch/if-else chains phức tạp | Khó mở rộng |
| **Speculative Generality** | Code "trường hợp" | Độ phức tạp không cần thiết |
| **Dead Code** | Code không sử dụng | Nhầm lẫn, gánh nặng duy trì |

### Các Bước Phân Tích

1. **Phân Tích Tự Động** (nếu scripts có sẵn)
   ```bash
   python scripts/detect-smells.py <file>
   ```

2. **Review Thủ Công**
   - Đi qua code một cách có hệ thống
   - Ghi chú mỗi smell với vị trí và mức độ nghiêm trọng
   - Phân loại theo tác động (Nguy Kịch/Cao/Trung Bình/Thấp)

3. **Ưu Tiên**
   Tập trung vào các smells mà:
   - Chặn phát triển hiện tại
   - Gây bugs hoặc nhầm lẫn
   - Ảnh hưởng đến các đường dẫn code được thay đổi nhiều nhất

### Đầu Ra: Báo Cáo Smell

Trình bày cho người dùng:
- Danh sách các smells được xác định với vị trí
- Đánh giá mức độ nghiêm trọng cho mỗi smell
- Thứ tự ưu tiên được khuyến nghị
- **Yêu cầu chấp thuận về các ưu tiên**

---

## Giai Đoạn 4: Tạo Kế Hoạch Refactoring

### Chọn Refactorings

Đối với mỗi smell, chọn một refactoring phù hợp từ catalog.

Xem [references/refactoring-catalog.md](../../../03-skills/refactor/references/refactoring-catalog.md) để có danh sách đầy đủ.

#### Smell-to-Refactoring Mapping

| Code Smell | Refactoring Khuyến Nghị |
|------------|---------------------------|
| Long Method | Extract Method, Replace Temp with Query |
| Duplicated Code | Extract Method, Pull Up Method, Form Template Method |
| Large Class | Extract Class, Extract Subclass |
| Feature Envy | Move Method, Move Field |
| Primitive Obsession | Replace Primitive with Object, Replace Type Code with Class |
| Long Parameter List | Introduce Parameter Object, Preserve Whole Object |
| Data Clumps | Extract Class, Introduce Parameter Object |
| Switch Statements | Replace Conditional with Polymorphism |
| Speculative Generality | Collapse Hierarchy, Inline Class, Remove Dead Code |
| Dead Code | Remove Dead Code |

### Cấu Trúc Kế Hoạch

Sử dụng mẫu tại [templates/refactoring-plan.md](../../../03-skills/refactor/templates/refactoring-plan.md).

Đối với mỗi refactoring:
1. **Mục Tiêu**: Code nào sẽ thay đổi
2. **Smell**: Vấn đề nào nó giải quyết
3. **Refactoring**: Kỹ thuật nào để áp dụng
4. **Các Bước**: Các micro-bước chi tiết
5. **Rủi Ro**: Điều gì có thể sai
6. **Hoàn Tác**: Cách hoàn tác nếu cần

### Cách Tiếp Theo Giai Đoạn

**QUAN TRỌNG**: Introduce refactoring tăng dần theo các giai đoạn.

**Giai Đoạn A: Quick Wins** (Rủi ro thấp, giá trị cao)
- Đổi tên biến để rõ hơn
- Extract code trùng lặp rõ ràng
- Loại bỏ dead code

**Giai Đoạn B: Cải Tiến Cấu Trúc** (Rủi ro trung bình)
- Extract methods từ các hàm dài
- Introduce parameter objects
- Move methods đến các lớp phù hợp

**Giai Đoạn C: Thay Đổi Kiến Trúc** (Rủi ro cao hơn)
- Thay thế conditionals với polymorphism
- Extract classes
- Introduce design patterns

### Điểm Quyết Định: Trình Bày Kế Hoạch Cho Người Dùng

Trước khi triển khai:
- Hiển thị kế hoạch refactoring hoàn chỉnh
- Giải thích mỗi giai đoạn và rủi ro của nó
- Nhận sự chấp thuận rõ ràng cho mỗi giai đoạn
- **Hỏi**: "Tôi có nên tiếp tục với Giai Đoạn A không?"

---

## Giai Đoạn 5: Triển Khai Tăng Dần

### Quy Tắc Vàng
> "Thay Đổi → Test → Xanh? → Commit → Bước tiếp theo"

### Nhịp Triển Khai

Đối với mỗi bước refactoring:

1. **Kiểm tra trước**
   - Tests đang pass (xanh)
   - Code biên dịch

2. **Thực hiện MỘT thay đổi nhỏ**
   - Làm theo các cơ chế từ catalog
   - Giữ thay đổi tối thiểu

3. **Xác Minh**
   - Chạy tests ngay lập tức
   - Kiểm tra lỗi biên dịch

4. **Nếu tests pass (xanh)**
   - Commit với thông điệp mô tả
   - Di chuyển đến bước tiếp theo

5. **Nếu tests fail (đỏ)**
   - DỪNG LẠI ngay lập tức
   - Hoàn tác thay đổi
   - Phân tích điều gì sai
   - Hỏi người dùng nếu không rõ

### Chiến Lược Commit

Mỗi commit nên là:
- **Nguyên Tử**: Một thay đổi logic
- **Có Thể Hoàn Tác**: Dễ dàng revert
- **Mô Tả**: Thông điệp commit rõ ràng

Ví dụ thông điệp commit:
```
refactor: Extract calculateTotal() from processOrder()
refactor: Rename 'x' to 'customerCount' for clarity
refactor: Remove unused validateOldFormat() method
```

### Báo Cáo Tiến Độ

Sau mỗi sub-giai đoạn, báo cáo cho người dùng:
- Các thay đổi được thực hiện
- Tests vẫn pass?
- Bất kỳ vấn đề nào gặp phải
- **Hỏi**: "Tiếp tục với batch tiếp theo?"

---

## Giai Đoạn 6: Review & Lặp Lại

### Checklist Sau Refactoring

- [ ] Tất cả tests pass
- [ ] Không có cảnh báo/lỗi mới
- [ ] Code biên dịch thành công
- [ ] Hành vi không thay đổi (xác minh thủ công)
- [ ] Tài liệu được cập nhật nếu cần
- [ ] Lịch sử commit sạch

### So Sánh Metrics

Chạy phân tích độ phức tạp trước và sau:
```bash
python scripts/analyze-complexity.py <file>
```

Trình bày cải tiến:
- Thay đổi số dòng code
- Thay đổi độ phức tạp vòng lục
- Thay đổi chỉ số khả năng duy trì

### Review Người Dùng

Trình bày kết quả cuối cùng:
- Tóm tắt tất cả thay đổi
- So sánh code trước/sau
- Cải tiến metrics
- Nợ kỹ thuật còn lại
- **Hỏi**: "Bạn có hài lòng với những thay đổi này không?"

### Các Bước Tiếp Theo

Thảo luận với người dùng:
- Có smells bổ sung để giải quyết không?
- Lên lịch refactoring tiếp theo?
- Áp dụng các thay đổi tương tự ở nơi khác?

---

## Hướng Dẫn Quan Trọng

### Khi DỪNG LẠI và Hỏi

Luôn dừng lại và tham khảo người dùng khi:
- Không chắc về logic kinh doanh
- Thay đổi có thể ảnh hưởng APIs bên ngoài
- Phủ vùng test không đủ
- Cần quyết định kiến trúc quan trọng
- Mức độ rủi ro tăng
- Bạn gặp độ phức tạp bất ngờ

### Quy Tắc An Toàn

1. **Không bao giờ refactor mà không có tests** (trừ khi người dùng thừa nhận rủi ro một cách rõ ràng)
2. **Không bao giờ thực hiện các thay đổi lớn** - chia thành các bước nhỏ
3. **Không bao giờ bỏ qua chạy test** sau mỗi thay đổi
4. **Không bao giờ tiếp tục nếu tests fail** - sửa hoặc hoàn tác trước
5. **Không bao giờ giả định** - khi nghi ngờ, hãy hỏi

### Những Gì KHÔNG Nên Làm

- Đừng kết hợp refactoring với việc thêm tính năng
- Đừng refactor trong các tình huống khẩn cấp của production
- Đừng refactor code mà bạn không hiểu
- Đừng over-engineer - giữ nó đơn giản
- Đừng refactor tất cả cùng một lúc

---

## Ví Dụ Bắt Đầu Nhanh

### Kịch Bản: Long Method với Duplication

**Trước:**
```javascript
function processOrder(order) {
  // 150 dòng code với:
  // - Logic xác thực trùng lặp
  // - Tính toán nội tuyến
  // - Trách nhiệm hỗn hợp
}
```

**Các Bước Refactoring:**

1. **Đảm bảo tests tồn tại** cho processOrder()
2. **Extract** xác thực vào validateOrder()
3. **Test** - nên pass
4. **Extract** tính toán vào calculateOrderTotal()
5. **Test** - nên pass
6. **Extract** thông báo vào notifyCustomer()
7. **Test** - nên pass
8. **Review** - processOrder() giờ điều phối 3 hàm rõ ràng

**Sau:**
```javascript
function processOrder(order) {
  validateOrder(order);
  const total = calculateOrderTotal(order);
  notifyCustomer(order, total);
  return { order, total };
}
```

---

## Tài Liệu Tham Khảo

- [Catalog Code Smells](../../../03-skills/refactor/references/code-smells.md) - Danh sách đầy đủ code smells
- [Catalog Refactoring](../../../03-skills/refactor/references/refactoring-catalog.md) - Các kỹ thuật refactoring
- [Mẫu Kế Hoạch Refactoring](../../../03-skills/refactor/templates/refactoring-plan.md) - Mẫu lập kế hoạch

## Scripts

- `scripts/analyze-complexity.py` - Phân tích metrics độ phức tạp code
- `scripts/detect-smells.py` - Phát hiện smell tự động

## Lịch Sử Phiên Bản

- v1.0.0 (2025-01-15): Phiên bản phát hành ban đầu với phương pháp luận Fowler, cách tiếp theo từng giai đoạn, các điểm tham khảo người dùng
