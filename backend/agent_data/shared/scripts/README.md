# 📁 shared/scripts/

这里存放贝塞尔龙虾编辑产出的口播稿和日报正文。

## 命名规范

- 口播稿：`script_YYYYMMDD.md`
- 日报正文：`daily_YYYYMMDD.md`

## 防重复机制

龙虾编辑每次被情报员唤醒后，会先检查当天的 `script_YYYYMMDD.md` 是否已存在。
如果存在，说明今天已经写过了，直接跳过，不重复执行。
