<font face='Times new roman'>

# Basic SQL Homework

<p align='right'>42227096 鄢怡然</p>

---
---

## 题目一（3分）

假设拟在数据库添加一个关系，其关系模式是 users(name, pswd, gender)，并让`name`作为主码。请使用`CREATE TABLE`命令添加该关系。

```sql
create table users
    (name  varchar(20) primary key,
     pswd  varchar(15) not null,
     gender varchar(1));
```

---

## 题目二（2分+3分）

考虑课堂中使用的`大学`数据库，包括如下关系：

- course(course_id, title, dept_name, credits)
- instructor(ID, name, dept_name, salary)
- teaches(ID, course_id, sec_id, semester, year)
- student(ID, name, dept_name, tot_cred)
- takes(ID, course_id, sec_id, semester, year, grade)

使用SQL语句完成下面的查询：

1. 找到在`计算机`学院开设的不少于`3`个`学分`的课程，并按`学分`进行升序排序。

```sql
select course_id, title, credits
from course
where dept_name = '计算机' 
      and credits >= 3
order by credits asc;
```

2. 找到所有被名叫`图灵`的老师教过的学生的学号（`ID`），并确保结果没有重复。

```sql
select student.ID
from takes, teaches, instructor, student
where instructor.name = '图灵'
      and instructor.ID = teaches.ID
      and teaches.course_id = takes.course_id
      and takes.ID = student.ID;
```

---

## 题目三（2分）

考虑题目二提到的关系模式，请问下面的SQL语句的含义是什么？

```sql
SELECT DISTINCT T.name
FROM instructor AS T, instructor AS S
WHERE T.salary > S.salary AND S.dept_name = '会计';
```

表示找到所有**薪资比会计学院`至少一位`教师工资高的教师姓名**。
