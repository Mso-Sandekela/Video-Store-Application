
--=========================================================================================
--Script file name: 4. Create_Insert_Procedure.sql
--Name & Surname: Sopumelela Sandekela
--Student number: CON-1475940-C5L6
--Date: 22/11/2023
--Description: This file will create a Stored Procedure Inserting a new pet type record.
--=========================================================================================

USE TygerValleyPetShelter --Call the Database for use...
GO

CREATE PROCEDURE sp_NewPetType
	@animType VARCHAR(30), --Declare the variable to use for populating 
	@animName VARCHAR(30), --inside the procedure.
	@stockLvl INT
AS
BEGIN

	IF (@animType != 'Bird') AND (@animType != 'Mammal') --If entered input is out of the required...
		BEGIN
		    RAISERROR('Entered value is not exccepted choose between pet species "Mammal" or "Bird".',16,1)
			RETURN --Returns custom made errorr...
		END

	IF (@animName = '') --If no value is added at all...
		BEGIN
			RAISERROR('No value has been entered, please enter animal name .',16,1)
			RETURN
		END


	IF (@stockLvl < 0 ) --Stock level can not be negetive...
		BEGIN
			RAISERROR('Stock level can not be that low',16,1)
			RETURN
		END


	INSERT INTO Animal( animType, animName, stockLvl )
	VALUES (@animType, @animName, @stockLvl)
--NOTE! variables are used as input devices accomodating change of values, 
--point of a procedure in all is rumming away from hard coded inputs

END
GO

--Executing the procedure.
EXEC sp_NewPetType 'Bird', 'Budgerigar', 16
GO
 PRINT 'New pet inserted successfully...'
GO

--Displaying the table...
SELECT *
FROM Animal
GO

--=========================================================================================
--INSERT STORED PROCEDURE COMPLETED SUCCESSFULLY...
--=========================================================================================



