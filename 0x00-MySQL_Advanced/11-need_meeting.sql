-- 0x00-MySQL_Advanced\11-need_meeting.sql
-- SQL script that creates a view need_meeting that lists all students that
-- have a score under 80 (strict) and no last_meeting or more than 1 month

-- Define the view
CREATE VIEW need_meeting AS
SELECT *
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
