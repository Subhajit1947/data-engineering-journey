CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      
SELECT
    IFNULL(
(
    SELECT
        salary 
    FROM
        (
        SELECT 
        *,dense_rank() over(order by salary desc) as rnk
        FROM Employee E
        )e
    where rnk=N
    limit 1
),null) as SecondHighestSalary

  );
END