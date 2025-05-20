# NoSQL Homework

<p align='right'>42227096 鄢怡然</p>

> 安装一个非关系型数据库（不限制），并完成简单的增、删、改、查。需要截图操作

## Neo4j图数据库

通过Neo4j Sandbox操作，使用Cypher查询

1. 创建项目
![image](https://github.com/user-attachments/assets/8bf2692c-fc54-4489-8640-9a7678f720f8)

2. 数据
   - 节点：类型/标签Person ，属性name、age
   - 关系：FRIEND

3.增
```cypher
CREATE (a:Person {name: '张三', age: 25})
CREATE (b:Person {name: '李四', age: 30})
WITH a, b
CREATE (a)-[:FRIEND]->(b)
RETURN a, b
```
![image](https://github.com/user-attachments/assets/836ca566-d533-4bea-b031-af15fb2b64dc)

![image](https://github.com/user-attachments/assets/83ec8b2f-c2da-494b-bb09-7add0a2a192f)

4. 改
```cypher
MATCH (a:Person {name: '张三'})
SET a.age = 26
RETURN a
```
![image](https://github.com/user-attachments/assets/ca26074e-2ad3-44ab-8346-fdea28968c96)

5. 查
```cypher
MATCH (p:Person)
RETURN p

MATCH (a:Person {name: '张三'})-[:FRIEND]->(b)
RETURN b.name AS FriendName
```
![image](https://github.com/user-attachments/assets/d5f82cec-035a-478e-ae6b-7aa9dcfa6f3e)

![image](https://github.com/user-attachments/assets/aa7acdd4-c24d-45b2-a6c4-f08a63febef6)

6. 删
```cypher
MATCH (p:Person {name: '张三'})-[r]-()
DELETE r, p
```
![image](https://github.com/user-attachments/assets/5a9a16f6-f610-4b79-9f03-bab7d89f7d4b)
