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