![image](https://github.com/user-attachments/assets/c3058742-a2e7-43e9-96a1-d608a53b614c)本周通过Postgresql软件实践基本的SQL，并学习了集合操作等知识。

# Lab Homework
<p align = 'right'>42227096 鄢怡然</p>

---
---

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
