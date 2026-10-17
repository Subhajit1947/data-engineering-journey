-- Write your PostgreSQL query statement below
WITH ss AS(
    SELECT 
        *
    FROM Students cross join Subjects
)

SELECT 
s.student_id,s.student_name,s.subject_name,
count(e.subject_name) as attended_exams
FROM ss s LEFT JOIN Examinations e
ON s.student_id=e.student_id and s.subject_name=e.subject_name
group by s.student_id,s.student_name,s.subject_name
order by student_id,subject_name
