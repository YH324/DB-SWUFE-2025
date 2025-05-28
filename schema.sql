-- project2025
-- 这是一个例子
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT,
  age INT,
  created_at TIMESTAMP
);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id),
  total_amount NUMERIC,
  status TEXT
);
