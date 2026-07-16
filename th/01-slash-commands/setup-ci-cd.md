<!-- i18n-source: 01-slash-commands/setup-ci-cd.md -->
<!-- i18n-date: 2026-05-08 -->
---
name: Setup CI/CD Pipeline
description: ติดตั้ง pre-commit hooks และ GitHub Actions สำหรับการประกันคุณภาพ
tags: ci-cd, devops, automation
---

# การติดตั้ง CI/CD Pipeline

ติดตั้ง DevOps quality gates ที่ครอบคลุม เหมาะสมกับประเภทโครงการ:

1. **วิเคราะห์โครงการ**: ตรวจจับภาษา framework build system และ tooling ที่มีอยู่
2. **กำหนดค่า pre-commit hooks** ด้วยเครื่องมือเฉพาะภาษา:
   - การจัดรูปแบบ: Prettier/Black/gofmt/rustfmt/etc.
   - Linting: ESLint/Ruff/golangci-lint/Clippy/etc.
   - ความปลอดภัย: Bandit/gosec/cargo-audit/npm audit/etc.
   - การตรวจสอบ type: TypeScript/mypy/flow (ถ้าใช้)
   - Tests: รัน test suites ที่เกี่ยวข้อง
3. **สร้าง GitHub Actions workflows** (.github/workflows/):
   - จำลอง pre-commit checks บน push/PR
   - matrix หลายเวอร์ชัน/แพลตฟอร์ม (ถ้าใช้)
   - การตรวจสอบการ build และ test
   - ขั้นตอน deployment (ถ้าจำเป็น)
4. **ตรวจสอบ pipeline**: ทดสอบในเครื่อง สร้าง test PR ยืนยันว่า checks ทั้งหมดผ่าน

ใช้เครื่องมือฟรี/open-source เคารพการกำหนดค่าที่มีอยู่ รักษาความเร็วในการรัน

---
**อัปเดตล่าสุด**: 9 เมษายน 2026
