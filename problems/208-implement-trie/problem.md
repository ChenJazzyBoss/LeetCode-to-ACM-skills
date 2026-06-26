# 208. 实现 Trie (前缀树)

**难度**：Medium
**知识点**：字典树、字符串、设计
**输入模式**：basic

## 题目描述

请你实现一个 Trie（前缀树），支持插入单词 `insert`、查找完整单词 `search`、判断前缀 `startsWith`。`search` 返回 `True`/`False`，`startsWith` 返回 `True`/`False`。

## 输入格式

第一行输入操作数 `q`。
接下来 `q` 行，每行一个操作：
- `INSERT word`
- `SEARCH word`
- `STARTSWITH prefix`

## 输出格式

按顺序输出每个 `SEARCH` 与 `STARTSWITH` 的结果，每行一个 `True`/`False`。

## 样例

**输入：**
```
5
INSERT apple
SEARCH apple
SEARCH app
STARTSWITH app
INSERT app
```

**输出：**
```
True
False
True
```

## 数据范围

- 1 ≤ q ≤ 10⁴
- 1 ≤ len(word) ≤ 100
