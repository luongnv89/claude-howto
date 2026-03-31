# 函数：`functionName`

## 描述
对该函数功能的简要描述。

## 函数签名
```typescript
function functionName(param1: Type1, param2: Type2): ReturnType
```

## 参数

| 参数名 | 类型 | 是否必填 | 描述 |
|-----------|------|----------|-------------|
| param1 | Type1 | 是 | param1 的描述 |
| param2 | Type2 | 否 | param2 的描述 |

## 返回值
**类型**：`ReturnType`

返回内容的描述。

## 异常（Throws）
- `Error`：当传入无效输入时
- `TypeError`：当传入错误类型时

## 示例

### 基础用法
```typescript
const result = functionName('value1', 'value2');
console.log(result);
```

### 高级用法
```typescript
const result = functionName(
  complexParam1,
  { option: true }
);
```

## 注意事项
- 附加说明或警告
- 性能注意事项
- 最佳实践

## 另请参阅
- [相关函数](#)
- [API 文档](#)
