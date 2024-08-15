--=========================================================================================
--Script file name: 7.2. Create_IterationReport_Procedure.sql
--Name & Surname: Sopumelela Sandekela
--Student number: CON-1475940-C5L6
--Date: 23/11/2023
--Description: This file will create a Stored Procedure for printing report 
--reading using Interaction method.
--=========================================================================================


USE TygerValleyPetShelter --Call database for use...
GO

SET NOCOUNT ON 
GO

--Create stored procedure for Report Interaction...
CREATE PROCEDURE sp_Report_Interaction
	@manID INT

AS
BEGIN

--Check if Manufacturer ID exists or no product is expired...
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

--Declare variables to used as output...
	DECLARE @compName VARCHAR(30),
			@contactNumber VARCHAR(15),
			@emalAddress VARCHAR(30),
			@foodID INT,
			@foodType VARCHAR(30),
			@totalRec INT --For calculating total number of record(s) expired at the end.

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

--Create  temporary table for easy manipulation, with required columns
	SELECT vw_ExpiredFoodDetails.FoodID, vw_ExpiredFoodDetails.CategoryName
	INTO #tempExpired
	FROM vw_ExpiredFoodDetails

--ADD column to label printer and unprinted records.
	ALTER TABLE #tempExpired
	ADD
	Printed SMALLINT

--Initialise all records as unlabeled by assigning 0 (Zero).
	UPDATE #tempExpired
	SET Printed = 0

	--Initialise totalRec for accumulation.
	SET @totalRec = 0 


--While printed is Zero(0) or while record unread.
--=======================================================
	WHILE EXISTS(SELECT *
			  FROM #tempExpired 
			  WHERE Printed = 0)

	BEGIN
	--Selects the lowest Manufacturing ID... 
		SELECT @foodID = MIN(#tempExpired.FoodID) 
		FROM #tempExpired
		WHERE (#tempExpired.Printed = 0)



		SELECT @foodType = #tempExpired.CategoryName
		FROM #tempExpired
		WHERE (@foodID = #tempExpired.FoodID)


--pRINT Each record linked to Manufacturer ID.
		PRINT CAST(@foodID AS VARCHAR) + SPACE(15 - LEN(@foodID)) + @foodType --Print current record...

--Accumulate total records read...
		SET @totalRec = @totalRec + 1

--Assign 1 on Printed column to labled that it's printed.
		UPDATE #tempExpired
		SET Printed = 1
		WHERE @foodID = #tempExpired.FoodID
	END
--End loop
--=======================================================

	--Print accumulated number...
	PRINT ''
	PRINT '_______________________________________'
	PRINT 'Total Records: '+ CAST(@totalRec AS VARCHAR)
	PRINT '_______________________________________'

--drops the temp table
	DROP TABLE #tempExpired

END
GO

--Execute Stored Procedure...
EXEC sp_Report_Interaction 7
GO

--NB: Some duplicated records will not show because 
--it the same food but was given to different animals
--Remember we are printing Expired food.

--=========================================================================================
--STORED PROCEDURE REPORT USING Interaction COMPLETED...
--=========================================================================================


