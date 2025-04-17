# w6:SQL Homework

---

<p align='right>42227096 鄢怡然</p>

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
- txt 数据文件
```txt

```

1. 使用`COPY`命令导入数据库（PostgreSQL）。

```sql
 \copy product(product_no, name, price) FROM 'C:\Users\weiqu\Desktop\product_list.txt' DELIMITER ',';
```
图
2. 将该关系导出为任意文件（如SQL、Txt、CSV、JSON等）。
```sql
 \copy product TO 'C:\Users\weiqu\DataGripProjects\04lab\output.csv' DELIMITER ',' ;
```
图

## 题目二（6分）

1. 添加一个新的商品，编号为`666`，名字为`cake`，价格不详。
```sql
INSERT INTO product VALUES
(666,'cake',null);
```
图
2. 使用一条SQL语句同时添加3个商品，内容自拟。
```sql
INSERT INTO product VALUES
(101,'juice',7),
(102,'chocolate',11),
(103,'mask',20);
```
图
3. 将商品价格统一打8折。
```sql
UPDATE product
SET price = price * 0.8
WHERE price IS NOT null ;
```
图
4. 将价格大于100的商品上涨2%，其余上涨4%。
```sql
UPDATE product
SET price = CASE
    WHEN price > 100 THEN price*1.02
    ELSE price*1.04
END
WHERE price IS NOT null;
```
图
5. 将名字包含`cake`的商品删除。
```sql
DELETE FROM product
WHERE name LIKE '%cake%';
```
图
6. 将价格高于平均价格的商品删除。
```sql
DELETE FROM product
WHERE price > (SELECT AVG(price)
               FROM product
               WHERE price IS NOT NULL);
```
图

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

比较`DELETE`和`TRUNCATE`的性能差异。


