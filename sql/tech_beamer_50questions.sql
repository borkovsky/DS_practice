-- Q-2. Write An SQL Query To Fetch “FIRST_NAME” From Worker Table In Upper Case.
SELECT upper(FIRST_NAME)
	FROM Worker;

-- Q-4. Write An SQL Query To Print First Three Characters Of  FIRST_NAME From Worker Table
SELECT substring(FIRST_NAME,1,3)
	FROM Worker;
-- Q-5. Write An SQL Query To Find The Position Of The Alphabet (‘A’) In The First Name Column 
-- ‘Amitabh’ From Worker Table.
Select INSTR(FIRST_NAME, BINARY'a') from Worker where FIRST_NAME = 'Amitabh';


-- Q-9. Write An SQL Query To Print The FIRST_NAME From Worker Table After Replacing ‘a’ With ‘A’.
Select REPLACE(FIRST_NAME,'a','A') from Worker;


-- Q-22

SELECT (first_name || ' ' || last_name) as full_NAME, salary
	FROM worker
WHERE salary BETWEEN 50000 AND 100000;

-- Q-36 Show second highest salary
Select max(Salary) from Worker 
where Salary not in (Select max(Salary) from Worker);

-- Q-37. Write An SQL Query To Show One Row Twice In Results From A Table.
SELECT first_name, department 
	FROM Worker W
 WHERE W.department = 'HR'
 UNION ALL
 	SELECT first_name, department
 	FROM Worker W1
 WHERE W1.department = 'HR';

 -- Q-40. Write An SQL Query To Fetch The Departments That Have Less Than Five People In It.
 SELECT department
	FROm worker
 GROUP BY department
 HAVING COUNT(worker_id) < 5;

 