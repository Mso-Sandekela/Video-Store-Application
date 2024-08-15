--=========================================================================================
--Script file name: 7.1. Create_CursorReport_Procedure.sql
--Name & Surname: Sopumelela Sandekela
--Student number: CON-1475940-C5L6
--Date: 23/11/2023
--Description: This file will create a Stored Procedure for printing report reading using cursor.
--=========================================================================================

USE TygerValleyPetShelter
GO

--Create procedure for Report Cursur printing...
CREATE PROCEDURE sp_Report_Cursor
	@manID INT

AS
BEGIN

--Check if entered Manufacturer ID is correct...
	IF NOT EXISTS (SELECT Manufacturer.manID 
					FROM Manufacturer
					JOIN Food
					ON Manufacturer.manID = Food.manID
					JOIN vw_ExpiredFoodDetails
					ON vw_ExpiredFoodDetails.FoodID = Food.foodID
					WHERE (Manufacturer.manID = @manID) AND (Food.foodID = vw_ExpiredFoodDetails.FoodID ))
	BEGIN
		RAISERROR ('Manufacturer does not have expired product(s) or Manucaturer ID does not exist.', 16, 1)
		RETURN
	END

--Create variables to use for output printing...
	DECLARE @compName VARCHAR(30),
			@contactNumber VARCHAR(15),
			@emalAddress VARCHAR(30),
			@foodID INT,
			@foodType VARCHAR(30),
			@totalRec INT

--Populuted variables that do not need redundance...
	SELECT  @compName = Manufacturer.compName,
			@contactNumber = Manufacturer.contactNo,
			@emalAddress = Manufacturer.emailAddress

	FROM Manufacturer
--Done with non-looping values...

--Printing Manufacturer Details, There is no repeating so no cursor is used...
	PRINT 'EXPIRED PRODUCTS REPORT:'
	PRINT '__________________________________________________________________________________'

	PRINT 'Generated:'
	PRINT GETDATE() --generates current date and time
	PRINT ''
	PRINT 'Company ID:		'	+ CAST(@manID AS VARCHAR)
	PRINT 'Company Name:	'	+ @compName
	PRINT 'Contact Number:	'	+ @contactNumber
	PRINT 'Email:			'	+ @emalAddress
	
--HEADER for The repeating output... 
	PRINT '__________________________________________________________________________________'
	PRINT 'Food ID		   Food Type'
	PRINT '__________________________________________________________________________________'

--Declaring Local cursor...
	DECLARE expiredFood_Cursor CURSOR LOCAL
	FOR SELECT vw_ExpiredFoodDetails.FoodID, vw_ExpiredFoodDetails.CategoryName 
		FROM vw_ExpiredFoodDetails
	FOR READ ONLY

	SET @totalRec = 0 --Assign total record for counting...

	OPEN expiredFood_Cursor --Open cursor for use...

	--Request first record...
	FETCH NEXT FROM expiredFood_Cursor
	INTO @foodID, @foodType 


	WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT CAST(@foodID AS VARCHAR) + SPACE(15 - LEN(@foodID)) + @foodType --Print current record...

			SET @totalRec = @totalRec + 1 --Accumulate total records read...

			--Request next record...
			FETCH NEXT FROM expiredFood_Cursor
			INTO @foodID, @foodType
		END

	PRINT ''
	PRINT '_______________________________________'
	PRINT 'Total Records:  '+ CAST(@totalRec AS VARCHAR)
	PRINT '_______________________________________'

	CLOSE expiredFood_Cursor
	DEALLOCATE expiredFood_Cursor

END
GO

EXEC sp_Report_Cursor 7
GO

--=========================================================================================
--STORED PROCEDURE REPORT USING CURSOR COMPLETED...
--=========================================================================================








