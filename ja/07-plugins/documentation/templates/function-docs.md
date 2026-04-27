<!-- i18n-source: 07-plugins/documentation/templates/function-docs.md -->
<!-- i18n-source-sha: 5caeff2 -->
<!-- i18n-date: 2026-04-27 -->

# 関数: `functionName`

## 説明
関数の動作の簡単な説明。

## シグネチャ
```typescript
function functionName(param1: Type1, param2: Type2): ReturnType
```

## パラメータ

| Parameter | Type | Required | 説明 |
|-----------|------|----------|-----|
| param1 | Type1 | Yes | param1 の説明 |
| param2 | Type2 | No | param2 の説明 |

## 戻り値
**Type**: `ReturnType`

返される値の説明。

## 例外
- `Error`: 不正な入力が与えられたとき
- `TypeError`: 誤った型が渡されたとき

## サンプル

### 基本的な使い方
```typescript
const result = functionName('value1', 'value2');
console.log(result);
```

### 応用的な使い方
```typescript
const result = functionName(
  complexParam1,
  { option: true }
);
```

## 補足
- 追加の注意事項や警告
- パフォーマンス上の考慮事項
- ベストプラクティス

## 関連項目
- [関連関数](#)
- [API ドキュメント](#)
