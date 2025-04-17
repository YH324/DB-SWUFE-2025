# w6:SQL Homework

---

<p align='right'>42227096 鄢怡然</p>

> 考虑关系模式`product(product_no, name, price)`，完成下面的题目：

## 题目一（4分）

在数据库中创建该关系，并自建上面关系的txt数据文件：

- 创建关系
```sql
CREATE TABLE product (
    product_no INT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL);
```
![a072a866596c9436d88b7a1dc951afc8](https://github.com/user-attachments/assets/d1868861-ca54-4d6e-a1ca-87ef04f9b455)

- txt 数据文件
```txt
1, "milk", 10.00
2, "bread", 15
3, "cup", 23
4, "bag", 44
5, "burger", 16
6, "beer", 19.9
7, "pencil", 4
```
![fe2a1179b73de0589603b3a647ff36bf](https://github.com/user-attachments/assets/e25611e8-983f-4f25-aa4b-b1921966076e)

1. 使用`COPY`命令导入数据库（PostgreSQL）。

```sql
 \copy product(product_no, name, price) FROM 'C:\Users\weiqu\Desktop\product_list.txt' DELIMITER ',';
```
![94e20a656a2bf4f3e67ce36fac24b706](https://github.com/user-attachments/assets/3d2be34c-c8b9-48ad-a60d-6d343fd1070a)

2. 将该关系导出为csv文件。
```sql
 \copy product TO 'C:\Users\weiqu\DataGripProjects\04lab\output.csv' DELIMITER ',' ;
```
![7e3cedda570ce4a3a5f610b1cda5555a](https://github.com/user-attachments/assets/c163f4c9-72a5-41e2-836b-55404e27bf82)
![45acfb396783f42ee00a8239fa7cfd4d](https://github.com/user-attachments/assets/594c8310-9157-486e-963e-d2d0ef0c4768)

## 题目二（6分）

1. 添加一个新的商品，编号为`666`，名字为`cake`，价格不详。
```sql
INSERT INTO product VALUES
(666,'cake',null);
```
![e14b51ca2c49e5d32ec5099455ec27ac](https://github.com/user-attachments/assets/29cebe13-2717-48c6-874c-d99685054535)

2. 使用一条SQL语句同时添加3个商品，内容自拟。
```sql
INSERT INTO product VALUES
(101,'juice',7),
(102,'chocolate',11),
(103,'mask',20);
```
![f08f1fa2093f4bde44840325570a4502](https://github.com/user-attachments/assets/7de9d07c-d99c-4a4f-a323-1f7c7058cc6d)

3. 将商品价格统一打8折。
```sql
UPDATE product
SET price = price * 0.8
WHERE price IS NOT null ;
```
![2ad67cf111847bbc05f8661f4020f48d](https://github.com/user-attachments/assets/3cdeeebf-35bf-4122-9121-ed567a177398)

4. 将价格大于100的商品上涨2%，其余上涨4%。
```sql
UPDATE product
SET price = CASE
    WHEN price > 100 THEN price*1.02
    ELSE price*1.04
END
WHERE price IS NOT null;
```
![beb88b951560ecde8ada0b7a053b19a8](https://github.com/user-attachments/assets/c90c0deb-36b5-47df-bd64-aa546d81fd89)

5. 将名字包含`cake`的商品删除。
```sql
DELETE FROM product
WHERE name LIKE '%cake%';
```
![068f10d342f044899784cb88e5254dcb](https://github.com/user-attachments/assets/d0e285a9-087c-4c0c-ac57-8783eeeade1f)

6. 将价格高于平均价格的商品删除。
```sql
DELETE FROM product
WHERE price > (SELECT AVG(price)
               FROM product
               WHERE price IS NOT NULL);
```
![1518f1bfcaeae03f182bb04bbd0e887b](https://github.com/user-attachments/assets/97775d25-5a22-4824-bd94-978f4529af6c)

## 题目三（5分）

### 针对PostgreSQL

使用参考下面的语句添加10万条商品，

```sql
-- PostgreSQL Only
INSERT INTO product (name, price)
SELECT
    'Product' || generate_series, -- 生成名称 Product1, Product2, ...
    ROUND((random() * 1000)::numeric, 2) -- 生成0到1000之间的随机价格，保留2位小数
FROM generate_series(1, 100000);
```
![image](https://github.com/user-attachments/assets/ff28850a-e9da-41ce-806a-0b635a1d1719)

比较`DELETE`和`TRUNCATE`的性能差异。

- `DELETE`
```sql
DELETE FROM product0;
```
![image](https://github.com/user-attachments/assets/e38cbbed-09bf-4ea8-8c0c-951697764ec5)

- `TRUNCATE`
```sql
TRUNCATE TABLE product0;
```
![image](https://github.com/user-attachments/assets/847a49d7-07c6-4658-9382-9c9c3d5454e0)

就删除整张表而言，truncate性能优于delete，delete优势在于删除表的部分或者条件触发。

