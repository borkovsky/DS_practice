#multiple table join
SELECT *
FROM table1
INNER JOIN table2 
   ON table1.pk = table2.fk
INNER JOIN table3 
   ON table1.pk = table3.fk
   AND table2.pk = table3.fk
