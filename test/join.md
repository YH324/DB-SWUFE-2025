# join 测试
<p align='right'>42227096 鄢怡然</p>

## 1. 大学数据库

  1. 展示每个教师（instructor ）的工号及其授课课程段（section）数量。如果仅考虑授课老师，使用单表查询完成。
```sql
SELECT teaches.id, COUNT(teaches.sec_id) AS section_count
FROM teaches
GROUP BY teaches.id;
```
![image](https://github.com/user-attachments/assets/fc697377-8438-4dc8-8b4b-85386a2b7277)

  2. 对于1，请确保即使没有授课的教师也要被输出。使用JOIN 完成。
```sql
SELECT instructor.id, COUNT(teaches.sec_id) AS section_count
FROM instructor
LEFT JOIN teaches ON instructor.id = teaches.id
GROUP BY instructor.id;
```
![image](https://github.com/user-attachments/assets/783b4537-ce1b-475e-b0fe-46530600eb4e)

  3. 请使用标量子查询（scalar subquery）完成第 2 题。
```sql
SELECT instructor.id,
       (SELECT COUNT(*)
        FROM teaches
        WHERE teaches.id = instructor.id) AS section_count
FROM instructor;
```
![image](https://github.com/user-attachments/assets/bff8ba3d-e65c-429f-a604-9e1f2ed51bc6)

  4. 解释为什么在 from 子句中追加 natural join section 并不会影响结果。
```sql
select course_id, semester, year, sec_id, avg (tot_cred)
 from takes natural join student
 where year = 2017
 group by course id, semester, year, sec id
 having count (ID) >= 2;
```
- `takes`结构：
![image](https://github.com/user-attachments/assets/ed5e6ecf-b271-43bc-b4bc-d419bd4ada06)
- `student`结构：
![image](https://github.com/user-attachments/assets/f3a811fb-31e5-4f7c-91f9-ae0b06b4c4c8)
- `section`结构：
![image](https://github.com/user-attachments/assets/5e179e9e-8e5f-4359-b606-841870845a85)

由于`natural join`会自然保留所有相同名称属性相等的值，根据以上展示的数据结构，在已有`from takes natural join student`的情况下，追加 natural join section不会带来更多影响查询的信息，即对`course_id`, `semester`, `year`, `sec_id`, `avg (tot_cred)`等不会有影响。

  5. 使用using重写
```sql
select *
from section natural join classroom
```
重写为：
```sql
select *
from section join classroom using (building);
```
![image](https://github.com/user-attachments/assets/9f3ba17f-baa0-4461-a3a3-bd99502e01ec)

---

## 2. 应用题
![image](https://github.com/user-attachments/assets/e1731e71-1ae4-4c80-90e2-59de0a269177)

1. 创建两个关系，并添加测试数据。其中emp_bonus 的内容严格按上表所示。
```sql
CREATE TABLE emp_bonus (
  emp_no INT PRIMARY  KEY,
  received VARCHAR(50),
  type INT);

CREATE TABLE emp(
  emp_no INT PRIMARY KEY,
  ename VARCHAR(50),
  sal DECIMAL,
  dept_no INT);
```
测试数据：
```sql
-- emp 
INSERT INTO emp (emp_no, ename, sal, dept_no) VALUES
(1001, 'Alice', 5000.00, 10),
(1002, 'Bob', 6000.00, 20),
(1003, 'Charlie', 5500.00, 10),
(1004, 'David', 6500.00, 30),
(1005, 'Eve', 7000.00, 20),
(1007, 'May', 7700.00, 42),
(1008, 'Tom', 8000.00, 42),
(1009, 'Fan', 7800.00, 42);

-- emp_bonus 
INSERT INTO emp_bonus (emp_no, received, type) VALUES
(1001, '01-MAR-2005', 1),
(1002, '02-MAY-2005', 2),
(1003, '02-MAY-2005', 1),
(1004, '04-JUN-2005', 2),
(1005, '01-SEP-2005', 1),
(1007, '01-MAR-2005', 1),
(1008, '02-MAY-2005', 2),
(1009, '04-JUN-2005', 3);
```
![image](https://github.com/user-attachments/assets/c303f1ae-96bd-43b4-a294-d8d598bce082)
![image](https://github.com/user-attachments/assets/d5e621d2-1632-4f53-9747-a9f217e25d58)

2. 请列出部门编号为42 的所有员工的总工资及其总奖金。
```sql
SELECT SUM(sal) as total_sal,
       SUM(CASE
               WHEN type = 1 THEN sal * 0.10
               WHEN type = 2 THEN sal * 0.20
               WHEN type = 3 THEN sal * 0.30
               ELSE 0
            END) as total_bonus
FROM emp JOIN emp_bonus USING(emp_no)
WHERE dept_no = 42;
```
![image](https://github.com/user-attachments/assets/78c9fd0b-8bad-403d-92d1-dc560640144e)

测试通过。
