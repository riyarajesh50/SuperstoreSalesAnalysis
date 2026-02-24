-- Sales by Category
SELECT Category, SUM(Sales) AS total_sales
FROM superstore
GROUP BY Category;

-- Regional Sales
SELECT Region, SUM(Sales) AS total_sales
FROM superstore
GROUP BY Region;

-- Discount vs Profit
SELECT Discount, AVG(Profit) AS avg_profit
FROM superstore
GROUP BY Discount
ORDER BY Discount;