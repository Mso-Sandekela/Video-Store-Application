--=========================================================================================
--Script file name: 5. Create_Update_Procedure.sql
--Name & Surname: Sopumelela Sandekela
--Student number: CON-1475940-C5L6
--Date: 22/11/2023
--Description: This file will create a Stored Procedure UPDATING a record on the Animal table.
--=========================================================================================


USE TygerValleyPetShelter
GO

CREATE PROCEDURE sp_UpdateStock
		@animID INT, 
		@num INT,
		@bitNum BINARY --Require values are only 1 and 0 in bit form 
AS                     --To indicate (1)Add, (0)Subtract.
BEGIN

	--iF THE USER ENTERED Animal ID number outside the existing IDs...
	IF NOT EXISTS( SELECT animID FROM Animal WHERE @animID = animID) 
	BEGIN
		RAISERROR('Your entered Pet ID that does not exists.',16,1)
		RETURN
	END

	IF (@num <= 0)--If user enters number less or equal to zero...
	BEGIN
		RAISERROR('Number to be added / subtracted can not be less than 1.',16,1)
		RETURN
	END


	IF (@bitNum = 0)--If bit number is 0 then run the Subtract batch...
	BEGIN
		UPDATE Animal
		SET stockLvl  = (stockLvl - @num)
		WHERE animID = @animID
	END
	ELSE --Else run the Add batch...
	BEGIN
		UPDATE Animal
		SET stockLvl = (stockLvl + @num)
		WHERE animID = @animID
	END

END
GO

--Executing the procedure, Adding 10 stocks on the Pet with animal ID 9...
EXEC sp_UpdateStock 9, 10, 1
GO

--Display Animal ID...
SELECT * 
FROM Animal

--=========================================================================================
--UPDATE Procedure COMPLETED SUCCESSFULLY...
--=========================================================================================

