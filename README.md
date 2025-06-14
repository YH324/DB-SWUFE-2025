# DB-SWUFE
Homework & Project & Self-Evaluation

## w1-intro

本周内容以宏观概念为主，通过老师的讲解和资料阅读，对数据库有了初步认识。

### 本周学习

建立对数据库的整体认知。

1. 数据可系统（数据库）
   - DBMS：数据管理系统
   - 数据及关联应用

2. 知识概念：
    - 数据抽象：学习了数据库系统的三层抽象结构（物理层、逻辑层、视图层），理解了“抽象”这一计算机科学核心思想如何帮助我们屏蔽底层复杂性。
    - 数据模型：关系模型（Relational Model）、实体-联系模型（E-R Model）、半结构化模型等。最常用的**关系模型**，即“表(table)”就是“关系(relation)”，由行（row/tuple）和列（column/attribute）构成。
    - SQL作为声明式语言（关注What，而非How）的两大组成部分：
      - **DDL（数据定义语言）**用于定义模式（`CREATE TABLE`）
      - **DML（数据操纵语言）**用于查询和更新（`SELECT`, `INSERT`）。
3. 为什么要用数据库？
   相比文件处理系统，DBMS的优越性在于解决了文件系统普遍存在的**数据冗余与不一致、数据隔离、访问困难、完整性、安全性和并发访问异常**等痛点。
   
### 实践

1. 环境搭建：遵循课程指引，成功在本地安装了ostgreSQL和DataGrip。
2. 挑战题：完成了 [第一周挑战题](https://github.com/YH324/DB-SWUFE-2025/blob/main/challenge/challenge-20250309.md)。主要是深化对DB的认识和熟悉LLM的API调用操作，对实际应用很有帮助。

### 小结

**关键词**：**数据库 (Database), DBMS**, 文件系统 vs. 数据库系统, 数据冗余与不一致, **数据抽象** (三层模型), 关系模型 (表/行/列), **DDL/DML**, SQL (声明式语言)

![](image/w1.png)

---

## w2-relational model

本周的学习深入到了抽象的**关系代数**，虽然完成了作业，但在初见关系代数时，确实感到了理论的挑战性，尤其是在并、交、差等集合运算上花费了较多时间才理清思路。

### 本周学习

1. 关系数据库
   - 结构：关系-表，属性-列，元组-行
   - 数据库模式-逻辑设计，数据库实例-数据快照
   - schema：含有关系名称和对应的属性集称为**该关系的模式**
      - instructor(ID, name, dept_name, salary) 
   
2.  码 (Key)/键：
    - 需要一个明确的标识符来区分每一条记录/元组。
    - 不同的码：
        - 超码 (Super Key)：能唯一标识元组的任意属性组合
        - 候选码 (Candidate Key)：**最小的超码**，真子集不可构成超码的超码
        - 主码 (Primary Key)：候选码中，由设计者选定的那一个
        - 外码 (Foreign Key)：是表与表之间建立连接的桥梁，它参照另一个表的主码，确保了数据的一致性

3.  关系代数：
    - DBMS在执行SQL查询时，会先将其翻译成关系代数的表示，再进行优化，理解它就是理解查询的本质。
    - 核心操作：
        - 选择行：$\sigma$，按行（水平）筛选出符合条件的元组
        - 选择列：$\pi$，按列（垂直）切出我们需要的属性
        - 连接 (Join, ⨝)：多表查询的核心，最常用的是自然连接，它能智能地将多个关系/表通过共同属性拼接起来
        - 并 (∪)、交 (∩)、差 (-)：对两个**相容**的表进行集合运算 （什么算相容？**关系的目相同，列名可以不同但实际含义相同，对应属性的类型相同**），还要巩固一下
     - ![eg](image/w2.png)

### 实践

完成了本周的 [Homework 1](homework/DBhomework01.md)。作业内容主要是将自然语言描述的查询需求，翻译成关系代数表达式。

### 小结

**关键词**：关系模式, 码, 关系代数

![](image/w2mermaid.png)

---

## w3-sql

学习了sql的基本语法和两类命令（DDL DML）

### 本周学习
1. 基本数据类型
   - 数字：int，smallint，**numeric(p,d)：最多p位，小数点后d位 PG中等价于`decimal`**，float(n)**1-24real，25-53 double precision**，real，double precision
   - 字符串：char（定长），varchar（可变长），text（任意长）
   - null
2. 模式定义
   ![eg1](image/w3eg1.png)
   - 约束：pk fk not null
   - 删除：
     ```sql
     -- 删除表
     drop table r;
     -- 清空数据，保留表
     delete from r; 
     ```
   ![eg2](image/w3eg2.png)

3. DML
   - 基本结构：select, from, where
      - 去除重复
        ```sql
        select distinct dept_name from instructor;
        ```
   - **字符串使用单引号！**
   - 不等于：! <>
   - between、行构造：
     ```sql
     select name from instructor
     where salary between 9000 and 10000;

     select course from section
     where (semester,year) = ('spring', 2018);
     ```
   - 多表查询

4. 更名
   - select dept_name as a;select name from instructor as T
   - 关系代数：$\rho_x(E)$，将E更名为x

5. 排序
   - order by xx desc, yy asc
   - 默认升序

### 实践

完成了本周的 [Homework 2](homework/DBhomework02.md)。

### 小结

**关键词**：基本类型（数，字符串）, DDL（create table） & DML（select，from，from）, 更名运算（as）, 排序字句（order by）
![](image/w3.png)

---

# w4 上机

重点学习：

- 连接数据库 & 执行 SQL
- 字符串操作
- SQL 集合操作（并、交、差）

### 本周学习

1. 连接数据库
   - PostgreSQL 环境：使用 Postgres.app 或 psql
   - 创建数据库：
     ```
     ![](image/w4eg1.png)
     ```bash
     CREATE DATABASE mydb;
     ```
   - 使用 DataGrip 连接数据库，Test Connection 成功后开始执行 SQL 文件（DDL.sql）

2. 导入数据（上机操作）
   - 执行语句文件：`DDL.sql`, `smallRelationsInsertFile.sql`
   - 设置数据源为 `mydb.public`

3. SQL 编写与执行
   - 建立Query Console
   - SELECT 语句练习：`distinct`, `between`, `where`, `and/or`, 多表查询
   - 更名操作：`AS`
   - 排序：`ORDER BY name DESC`

4. **字符串操作**
   - 字符串区分大小写
   - 如果字符串里有单引号，则double：`I''m good`；如果有双引号，不变
   - pg区分字符串大小写
   - boolean有三种状态
   - 常用字符串函数：
     ```sql
     SELECT lower('CHINA'), upper('good');
     SELECT trim(' SWUFE ');
     SELECT dept_name, length(dept_name) FROM department;
     ```
   - 模糊查询：
     - `%` 任意长度字符串，`_` 任意单字符
     - `LIKE`, `NOT LIKE`
     - 转义 `%`：`LIKE 'abc\%d%'`

5. **拼接与 CASE 表达式**
   - 拼接符号：`||`
     ```sql
     SELECT name || ' from ' || dept_name FROM student WHERE tot_cred > 50;
     ```
   - `CASE` 多分支分类：
     ```sql
     SELECT id,
       CASE
         WHEN score < 60 THEN 'C'
         WHEN score >= 80 THEN 'A'
         ELSE 'B'
       END
     FROM marks;
     ```

6. **集合操作**
   - `UNION`：并
   - `INTERSECT`：交
   - `EXCEPT`：差（MySQL不支持）

### 实践

完成了本周的 [Homework 3](homework/DBhomework03.md)，涵盖了一些上机操作和模糊查询。

### 小结

关键词：**连接数据库**、SQL 文件执行、字符串函数、**模糊匹配**、拼接符、集合操作（UNION/INTERSECT/EXCEPT）、CASE 分类语句
![](image/w4.png)

---

## w5、6-聚合查询与增删改

### 学习

1. null 值处理
   - null 表示“缺失值”，具有**反直觉特性**
     - `1 + null → null`、`1 > null → unknown`
   - 布尔三值逻辑：`true / false / unknown(null)`
   - 不能用 `=` 或 `<>` 比较 null，需使用：
     ```sql
     salary IS NULL / IS NOT NULL
     ```
   - `distinct` 视多个 null 为相等
   - order by 可能会把null排前面

2. coalesce 与 CASE 替代
   - `coalesce(x, y)`：若 x 为 null，返回 y
   - 等价 CASE：
     ```sql
     CASE WHEN salary IS NULL THEN 0 ELSE salary END
     ```

3. 聚集函数
   - 常用：`avg`, `sum`, `count`, `min`, `max`
   - 忽略 null（除 `count(*)` 会统计 null）
     ```sql
     SELECT count(*), count(salary) FROM instructor;
     ```
     **仅count能与\* 连用，仅count(\* )考虑null**
   - 聚集不能直接出现在where，因为谓词字句比聚集先生效
4. 分组聚集
   - 使用 `GROUP BY` 进行分组统计：
     ```sql
     SELECT dept_name, avg(salary) 
     FROM instructor 
     GROUP BY dept_name;
     ```
   - `HAVING` 作用于聚集后的分组，用于限制分组：
     ```sql
     HAVING avg(salary) > 50000
     ```
   - **出现在select但没有被聚集的属性必须出现在group by**

5. 嵌套子查询
   - 可嵌套于 `from`, `where`, `select`
   - `with` 语句定义临时关系
   - **标量子查询**：返回单值，用作比较条件
     ```sql
     SELECT name FROM instructor
     WHERE salary > (SELECT min(salary) FROM instructor);
     ```

6. 集合操作与比较
   - IN / NOT IN：成员资格判断
   - > SOME / > ALL：
     - `> SOME (...)` 相当于比其中**至少一个大**
     - `> ALL (...)` 比所有都大
   - `= SOME` ≈ `IN`，`<> ALL` ≈ `NOT IN`
   - any等价some

7. 空关系测试（EXISTS）
```sql
SELECT ... WHERE EXISTS (SELECT 1 FROM xxx);
```
用于判断子查询是否非空，比 `IN` 更高效

8. SQL 修改数据库（w6 重点）
- 删
  ```sql
  DELETE FROM instructor WHERE salary > 80000;
  -- 区别drop 和delete
  ```
- 增
  ```sql
  --指定，可以不指定但要按顺序
  INSERT INTO course(course_id, title) VALUES (...);
  INSERT INTO instructor SELECT ... FROM student;
  ```
- 改
  ```sql
  UPDATE instructor SET salary = salary * 1.05;
  ```
- 批量插入导入：使用 `COPY` 更快

9. DDL 扩展：修改关系
- 添加字段：
  ```sql
  ALTER TABLE student ADD COLUMN nationality text;
  ```
- 删除字段（ALTER TABLE student DROP COLUMN nationality）、修改数据类型、字段重命名
  ![](image/w56eg1.png)
- 添加约束：
  - `UNIQUE`, `CHECK`, `DEFAULT`
  - `ALTER TABLE ... ADD CONSTRAINT ...`

10. SQL 排名（RANK）
- 使用窗口函数：
  ```sql
  RANK() OVER (ORDER BY salary DESC)
  ```
**select 字句的alias（重命名）不能用于where**

### 小结

关键词：**`null`**、三值逻辑、`coalesce`、**聚集函数**、分组聚集、`having`、**嵌套子查询**、`> some`、`exists`、`insert/delete/update`、`alter table`、约束、rank 排名
![](image/w56.png)

---

## w7、8-多表JOIN与查询优化



