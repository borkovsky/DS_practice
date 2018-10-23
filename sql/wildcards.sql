#Wildcards

-- Select all records where the second letter of the City is an "a".

SELECT *
	FROM Customers
 WHERE City LIKE '_a%';


-- Select all records where the first letter of the City is an "a" or a "b" or a "c".
SELECT *
	FROM Customers
 WHERE City LIKE '[abc]';

-- Select all records where the first letter of the City starts with anything from an "a" to an "f".
SELECT *
	FROM Customers
 WHERE City LIKE '[a-f]%';

-- Select all records where the first letter of the City is NOT an "a" or a "b" or a "c".
SELECT *
	FROM Customers
 WHERE City LIKE '[d-z]%'

#OR
SELECT *
	FROM Customers
 WHERE City LIKE '[!abc]%'