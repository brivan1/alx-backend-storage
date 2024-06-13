-- create a function t that divides 2 number
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE results FLOAT DEFAULT 0;

	IF b != 0 THEN
		SET results = a/b;
	END IF;
	RETURN results;
END $$
DELIMITER ;
