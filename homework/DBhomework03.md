# Lab_SQL Homework
<p align = 'right'>42227096 鄢怡然</p>

---
---

## 题目一（3分+1分）

> **需要**使用PostgreSQL/MySQL及DataGrip软件操作，并对操作页面及结果进行截图。

1. 新建一个`university`数据库，并执行`largeRelationsInsertFile.sql`，导入数据。

   - 新建一个`university`数据库
![alt text](<}{FA)_73G~{GA{60~1]@{71.png>)
![alt text](<)[KCB@1~%C~YJANV7DR%H3E.png>)
   - 执行`largeRelationsInsertFile.sql`，导入数据
![alt text](T}@4U$V]AG%JE}$LY4GOX@M.png)

    **完成**

2. 运行第2次作业的题目三代码。注意：把原题目中的`会计`改成`History`。

```sql
SELECT DISTINCT T.name
FROM instructor AS T, instructor AS S
WHERE T.salary > S.salary AND S.dept_name = 'History';
```

表示找到所有**薪资比历史学院`至少一位`教师工资高的教师姓名**。

---

## 题目二（3分）

### PostgreSQL

参考[Pattern Matching](https://www.postgresql.org/docs/17/functions-matching.html)，在PG中使用至少三种方法实现找到所有以`S`开头教师的名字。
1. LIKE
```sql
SELECT name FROM instructor
WHERE name LIKE 'S%';
```
查询结果

2. SIMILAR TO
```sql
SELECT name FROM instructor
WHERE name SIMILAR TO 'S%';
```
查询结果

3. POSIX Regular Expressions
```sql
SELECT name FROM instructor
WHERE name ~ '^S';
```
查询结果

---

## 题目三（3分）

`psql`是PostgreSQL的命令行工具，请使用`psql`命令行工具：

1. 实现题目二

连接数据库`university`
```
Server [localhost]:
Database [postgres]: university
Port [5432]:
Username [postgres]:
用户 postgres 的口令：
```
执行题目二查询语句，查询及结果如下：
    
```
university=# SELECT name FROM instructor
university-# WHERE name LIKE 'S%';
       name
-------------------
 Shuming
 Sullivan
 Soisalon-Soininen
 Sarkar
 Sakurai
(5 行记录)


university=# SELECT name FROM instructor
university-# WHERE name SIMILAR TO 'S%';
       name
-------------------
 Shuming
 Sullivan
 Soisalon-Soininen
 Sarkar
 Sakurai
(5 行记录)


university=# SELECT name FROM instructor
university-# WHERE name ~ '^S';
       name
-------------------
 Shuming
 Sullivan
 Soisalon-Soininen
 Sarkar
 Sakurai
(5 行记录)
```

2. 列出所有的数据库
使用`\l`命令
```
postgres=# \l
                                                     数据库列表
    名称    |  拥有者  | 字元编码 | Locale Provider | 校对规则 | Ctype | Locale | ICU Rules |       存取权限
------------+----------+----------+-----------------+----------+-------+--------+-----------+-----------------------
 mydb       | postgres | UTF8     | libc            | zh-CN    | zh-CN |        |           |
 postgres   | postgres | UTF8     | libc            | zh-CN    | zh-CN |        |           |
 template0  | postgres | UTF8     | libc            | zh-CN    | zh-CN |        |           | =c/postgres          +
            |          |          |                 |          |       |        |           | postgres=CTc/postgres
 template1  | postgres | UTF8     | libc            | zh-CN    | zh-CN |        |           | =c/postgres          +
            |          |          |                 |          |       |        |           | postgres=CTc/postgres
 university | postgres | UTF8     | libc            | zh-CN    | zh-CN |        |           |
(5 行记录)
```

3. 列出当前数据库的所有表
以数据库`university`为例，使用`\d`命令
```
university=# \d
                 关联列表
 架构模式 |    名称    |  类型  |  拥有者
----------+------------+--------+----------
 public   | advisor    | 数据表 | postgres
 public   | classroom  | 数据表 | postgres
 public   | course     | 数据表 | postgres
 public   | department | 数据表 | postgres
 public   | instructor | 数据表 | postgres
 public   | prereq     | 数据表 | postgres
 public   | section    | 数据表 | postgres
 public   | student    | 数据表 | postgres
 public   | takes      | 数据表 | postgres
 public   | teaches    | 数据表 | postgres
 public   | time_slot  | 数据表 | postgres
(11 行记录)
```

4. 显示某张表的关系模式
以数据库`university`下的`instructor`为例，使用`\d instructor`命令
```
university=# \d instructor
                   数据表 "public.instructor"
   栏位    |         类型          | 校对规则 |  可空的  | 预设
-----------+-----------------------+----------+----------+------
 id        | character varying(5)  |          | not null |
 name      | character varying(20) |          | not null |
 dept_name | character varying(20) |          |          |
 salary    | numeric(8,2)          |          |          |
索引：
    "instructor_pkey" PRIMARY KEY, btree (id)
检查约束限制
    "instructor_salary_check" CHECK (salary > 29000::numeric)
外部键(FK)限制：
    "instructor_dept_name_fkey" FOREIGN KEY (dept_name) REFERENCES department(dept_name) ON DELETE SET NULL
由引用：
    TABLE "advisor" CONSTRAINT "advisor_i_id_fkey" FOREIGN KEY (i_id) REFERENCES instructor(id) ON DELETE SET NULL
    TABLE "teaches" CONSTRAINT "teaches_id_fkey" FOREIGN KEY (id) REFERENCES instructor(id) ON DELETE CASCADE
```

Hint: [psql](https://www.postgresql.org/docs/current/app-psql.html), [mysql shell](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-commands.html)
