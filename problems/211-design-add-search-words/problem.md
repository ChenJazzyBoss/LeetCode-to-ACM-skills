# 211. 添加与搜索单词 - 数据结构设计

**难度**：Medium
**知识点**：字典树、字符串、DFS
**输入模式**：basic

## 题目描述

设计一个支持 `addWord(word)` 与 `search(word)` 的数据结构。`search` 可以包含 `'.'` 通配符，`'.'` 可以匹配任意一个字母。返回 `True`/`False`。

## 输入格式

第一行输入操作数 `q`。
接下来 `q` 行，每行：
- `ADD word`
- `SEARCH word`

## 输出格式

按顺序输出每个 `SEARCH` 结果，每行一个 `True`/`False`。

## 样例

**输入：**
```
4
ADD bad
SEARCH bad
SEARCH b.d
SEARCH .ad
```

**输出：**
```
True
True
True
```

## 数据范围

- 1 ≤ q ≤ 10⁴
- 1 ≤ len(word) ≤ 25
