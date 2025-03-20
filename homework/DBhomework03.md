# Lab_SQL Homework
<p align = 'right'>42227096 鄢怡然</p>

---
---

## 题目一（3分+1分）

> **需要**使用PostgreSQL及DataGrip软件操作，并对操作页面及结果进行截图。

1. 新建一个`university`数据库，并执行`largeRelationsInsertFile.sql`，导入数据。
2. 运行第2次作业的题目三代码。注意：把原题目中的`会计`改成`History`。

## 题目二（3分）

参考[Pattern Matching](https://www.postgresql.org/docs/17/functions-matching.html)，在PG中使用至少三种方法实现找到所有以`S`开头教师的名字。

## 题目三（3分）

`psql`是PostgreSQL的命令行工具。请使用`psql`命令行工具：

- 实现题目二
- 列出所有的数据库
- 列出当前数据库的所有表
- 显示某张表的关系模式


---
---

待更新：
## 题目一（2分）
完成第2次作业的题目一。
> 假设拟在数据库添加一个关系，其关系模式是 users(name, pswd, gender)，并让`name`作为主码。请使用`CREATE TABLE`命令添加该关系。
```sql
create table users
    (name  varchar(20) primary key,
     pswd  varchar(15) not null,
     gender varchar(1));
```
完成

---

## 题目二（3分+1分）
1. 新建一个`university`数据库，并执行`largeRelationsInsertFile.sql`，导入数据。
- 新建一个`university`数据库
完成

- 执行`largeRelationsInsertFile.sql`，导入数据
运行`largeRelationsInsertFile.sql`
运行成功
运行结果

完成


2. 运行第2次作业的题目三代码。注意：把原题目中的`会计`改成`History`。
```sql
SELECT DISTINCT T.name
FROM instructor AS T, instructor AS S
WHERE T.salary > S.salary AND S.dept_name = 'History';
```
表示找到所有**薪资比历史学院`至少一位`教师工资高的教师姓名**。

运行
运行成功
结果
完成

---

## 题目三（2分+2分）
1. 通过实验验证PG中`like`是大小写敏感的。
以`History`为例，接题目二创建的数据库和导入数据，首先模糊查询学院为`His`开头的全部信息:
```sql
SELECT * FROM department
WHERE dept_name LIKE 'His%';
```
结果如下：

把`His%`改为`his%`，执行相同查询:
```sql
SELECT * FROM department
WHERE dept_name LIKE 'his%';
```
结果如下：

对比两次查询结果不同，可验证PG中`like`是大小写敏感的

2. 在`university`数据库中查询所有包含名字`sci`的学院名称（`dept_name`），而不区分大小写。
```sql
SELECT dept_name FROM department
WHERE lower(dept_name) LIKE '%sci%';
```
完成
