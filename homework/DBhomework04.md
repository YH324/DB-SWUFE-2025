# w5:SQL Homework

<p align='right'>42227096 鄢怡然</p>

---

## 题目一（2分）

> 请问下面的SQL语句是否合法？用实验验证你的想法。你从实验结果能得到什么结论？

```sql
SELECT dept_name, min(salary)
FROM instructor;

SELECT dept_name, min(salary)
FROM instructor
GROUP BY dept_name
HAVING name LIKE '%at%';

SELECT dept_name
FROM instructor
WHERE AVG(salary) > 20000;
```

- 第一句不合法，`SELECT`的子句属性如果没有在聚集函数中，就要出现在`GROUP BY`子句
![](../image/4.1.1.1.png)
**添加GROUP BY后**
![](../image/4.1.1.2.png)
- 第二句不合法，出现在`HAVING`子句且没有被聚集的属性只能出现在`GROUP BY`子句
![](../image/4.1.2.1.png)
**添加GROUP BY name后**
![](../image/4.1.2.2.png)
- 第三句不合法，`WHERE`子句谓词生效早于聚合函数，即`>`先生效，所以聚合函数不可放在`WHERE`子句中。
![](../image/4.1.3.1.png)
**改成HAVEING子句,添加GROUP BY和SELECT属性**
![](../image/4.1.3.2.png)
---

## 题目二（3分+3分+2分）

> 1. 找到工资最高员工的名字，假设工资最高的员工只有一位（至少两种写法）。
> 2. 找到工资最高员工的名字，假设工资最高的员工有多位（试试多种写法）。
> 3. 解释下面四句。

```sql
SELECT 1 IN (1);

SELECT 1 = (1);

SELECT (1, 2) = (1, 2);

SELECT (1) IN (1, 2);
```

1. 两种写法：
   - 子查询+WHERE
```sql
SELECT DISTINCT name,salary
FROM instructor
WHERE salary = (SELECT max(salary)
                FROM instructor);
```
![](../image/4.2.1.1.png)
   - ORDER BY + LIMIT 1
```sql
SELECT name, salary
FROM instructor
ORDER BY salary DESC
LIMIT 1;
```
![](../image/4.2.1.2.png)

2. 4种写法：
   - 子查询 + WHERE
```sql
SELECT name,salary
FROM instructor
WHERE salary = (SELECT max(salary)
                FROM instructor);
```
![](../image/4.2.2.1.png)
   - ORDER BY + LIMIT 10
```sql
SELECT name, salary
FROM instructor
ORDER BY salary DESC
LIMIT 10;
```
先找最高的10位，发现最高的只有1位；如果存在多位最高者，根据查询结果调整LIMIT子句
![](../image/4.2.2.2.png)
   - ALL
```sql
SELECT name, salary
FROM instructor
WHERE salary >= ALL (SELECT salary FROM instructor);
```
![](../image/4.2.2.3.png)
   - JOIN
```sql
SELECT i.*
FROM instructor i
         JOIN (SELECT MAX(salary) AS max_salary FROM instructor) m
              ON i.salary = m.max_salary;
```

3. 解释：
   - `SELECT 1 IN (1);`：查询值`1`是否在`集合（1）`中
返回true
![](../image/4.2.3.1.png)
   - `SELECT 1 = (1);`：查询值`1`是否等于`（1）`，`（1）`会被解析为值1
返回true
![](../image/4.2.3.2.png)
   - `SELECT (1, 2) = (1, 2);`：查询`(1, 2)`长度及对应元素位置是否与`(1, 2)`完全一致
返回true
![](../image/4.2.3.3.png)
   - `SELECT (1) IN (1, 2);`：查询`(1)`是否在`集合(1, 2)`中，`（1）`会被解析为值1
返回true
![](../image/4.2.3.4.png)
