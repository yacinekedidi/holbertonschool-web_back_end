-- a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
IF EXISTS (SELECT * FROM users WHERE id = user_id) THEN
    UPDATE users
    SET average_score=(SELECT AVG(score) FROM corrections AS c WHERE c.user_id = user_id)
    WHERE id = user_id;
END IF;
END;
$$
