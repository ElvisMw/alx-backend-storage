-- 0x00-MySQL_Advanced\11-need_meeting.sql
-- SQL script that creates a view need_meeting that lists all students that
-- have a score under 80 (strict) and no last_meeting or more than 1 month.
-- Requirements: The view need_meeting should return all students name when:
-- They score are under (strict) to 80
-- AND no last_meeting date OR more than a month

DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    UPDATE users set average_score = (SELECT
    SUM(corrections.score * projects.weight) / SUM(projects.weight)
    FROM corrections
    INNER JOIN projects
    ON projects.id = corrections.project_id
    where corrections.user_id = user_id)
    where users.id = user_id;
END $$
DELIMITER ;