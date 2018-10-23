-- Which supplier of three or more products has the highest average product price?
SELECT
    SupplierName,
    COUNT(*) as NumProducts,
    AVG(p.Price) as MeanPrice
FROM
    Suppliers AS s
  JOIN
    Products AS p
  ON
    s.SupplierID = p.SupplierID
GROUP BY
    s.SupplierID
HAVING
    NumProducts >= 3
ORDER BY
    MeanPrice DESC;
