use video_store;

DELIMITER //

DROP PROCEDURE IF EXISTS sp_HireOutMovie;

CREATE PROCEDURE sp_HireOutMovie(IN num VARCHAR(10),
								 IN vidID INT)
BEGIN
	DECLARE id INT;
    DECLARE ver INT;

	SELECT custID INTO id FROM customers WHERE phone = num;
    
    SELECT VideoVer INTO ver FROM video WHERE videoId = vidID;
    
    INSERT INTO hire VALUES ( id, vidID, ver, current_date(), NULL);
    
END //

DELIMITER ;



