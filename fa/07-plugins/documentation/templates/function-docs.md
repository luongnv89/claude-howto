# تابع: `functionName`

## توضیح
توضیح مختصری از اینکه این تابع چه کاری انجام می‌دهد.

## امضا
```typescript
function functionName(param1: Type1, param2: Type2): ReturnType
```

## پارامترها

| پارامتر | نوع | الزامی | توضیح |
|---------|------|----------|-------------|
| param1 | Type1 | بله | توضیح param1 |
| param2 | Type2 | خیر | توضیح param2 |

## بازگشتی
**نوع**: `ReturnType`

توضیح چیزی که بازگردانده می‌شود.

## استثناها
- `Error`: هنگامی که ورودی نامعتبر ارائه شود
- `TypeError`: هنگامی که نوع اشتباه ارسال شود

## نمونه‌ها

### استفاده پایه
```typescript
const result = functionName('value1', 'value2');
console.log(result);
```

### استفاده پیشرفته
```typescript
const result = functionName(
  complexParam1,
  { option: true }
);
```

## یادداشت‌ها
- یادداشت‌ها یا هشدارهای اضافی
- ملاحظات عملکرد
- بهترین روش‌ها

## همچنین ببینید
- [تابع مرتبط](#)
- [مستندات API](#)

---

**آخرین به‌روزرسانی**: ۴ اوت ۲۰۲۶
**نسخه Claude Code**: 2.1.220
**منابع**:
- https://code.claude.com/docs/en/plugins
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
