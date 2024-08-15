--=========================================================================================
--Script file name: 6. Create_Delete_Procedure.sql
--Name & Surname: Sopumelela Sandekela
--Student number: CON-1475940-C5L6
--Date: 23/11/2023
--Description: This file will create a Stored Procedure to 
--Delete a specified food type and all dependent/child records.
--=========================================================================================

USE TygerValleyPetShelter-- Call the database for use...
GO

CREATE PROCEDURE sp_DeleteFoodType 
--Create variables to compare with whenever user whats to delete any type user chooses...
--Use ID to get it get from tables where its referenced...
	@foodID INT,
	@foodType VARCHAR(30)  
AS
BEGIN

	--DELETE record on parent table...
	IF EXISTS (SELECT VW_ExpiredFoodDetails.CategoryName 
				FROM VW_ExpiredFoodDetails 
				WHERE vw_ExpiredFoodDetails.FoodID = @foodID)
	BEGIN

	--Delete record related to Food locating by @foodID [Child Table]...
		DELETE 
		FROM FoodDonationDetails
		WHERE (FoodDonationDetails.foodID = @foodID) 

	--DELETE record on [Parent Table]...
		DELETE 
		FROM Food
		WHERE Food.foodType = @foodType
		AND (Food.foodID = @foodID)

	END
	ELSE
	BEGIN
		RAISERROR ('Food type does not exist on the table, otherwise double check if its between "Mammal" and "Bird"', 16, 1)
		RETURN
	END


END
GO
PRINT 'Expired specified food type deleted successfully...'
GO

--Test Delete Stored Procedure...
EXEC sp_DeleteFoodType 16, 'Seed'

SELECT *
FROM vw_ExpiredFoodDetails

--=========================================================================================
--[DELETE PROCEDURE]
--=========================================================================================



