--=========================================================================================
--Script file name: 3. Create_Views.sql
--Name & Surname: Sopumelela Sandekela
--Student number: CON-1475940-C5L6
--Date: 20/11/2023
--Description: This SQL script file will create a Views for different scenarios specified 
--on Tygervalley Pet Shelter (TPS) Database requirements.
--=========================================================================================

USE TygerValleyPetShelter
GO

--vw_ManufacturerDetails VIEW
--============================

/*In Case of calling The view with SELECT statement more than once
Allows the code to be re-ran.*/
IF EXISTS (SELECT Table_Name FROM Information_Schema.views
		WHERE TABLE_NAME = 'vw_ManufacturerDetails')
BEGIN
  DROP View vw_ManufacturerDetails
  PRINT 'View vw_Manufacturer droped successfully...'
  PRINT ' '
END
GO

--Creating View vw_ManufacturerDetails...
CREATE VIEW vw_ManufacturerDetails
AS
 
  SELECT Manufacturer.manID CompanyID, Manufacturer.compName CompanyName, 
		Manufacturer.contactNo ContactNumber, Manufacturer.emailAddress,
		Food.foodType FoodType, Food.foodID FoodID, FoodDonationDetails.quantity AmountPerCategory
   FROM Manufacturer
   JOIN Food 
   ON Manufacturer.manID = Food.manID
   JOIN FoodDonationDetails
   ON FoodDonationDetails.foodID = Food.foodID
		
GO
	PRINT 'View vw_ManufacturerDetails created successfully...'
GO
--Calling the View with SELECT statement...
	SELECT * FROM vw_ManufacturerDetails
GO
--=========================================================================================

--vw_PetsPerType VIEW
--============================

--DROP the View if it exist...
IF EXISTS(SELECT Table_Name FROM Information_Schema.views
		  WHERE Table_Name = 'vw_PetsPerType')
BEGIN
	DROP VIEW vw_PetsPerType
	PRINT 'View vw_PetsPerType droped successfully...'
END
GO

--Creating the vw_PetsPerType View...
CREATE VIEW vw_PetsPerType
AS

	SELECT Animal.animType AnimalType, Animal.stockLvl TotalAnimal, 
		   Animal.animID CategoryID, Animal.animName CategoryName
	FROM Animal

GO
	PRINT 'View vw_PetsPerType created successfully'
GO
--Calling the View with SELECT statement...
	SELECT * FROM vw_PetsPerType
GO
--=========================================================================================

--vw_ExpiredFoodDetails
--============================

--Drop View if exist...
IF EXISTS(SELECT Table_Name FROM INFORMATION_SCHEMA.VIEWS
		  WHERE Table_Name = 'vw_ExpiredFoodDetails')
BEGIN
	DROP VIEW  vw_ExpiredFoodDetails
	PRINT 'View  vw_ExpiredFoodDetails droped successfully...'
	PRINT ' '
END
GO

--Create view for vw_ExpiredFoodDetails...
CREATE VIEW  vw_ExpiredFoodDetails
AS

	SELECT Manufacturer.compName CompanyName, Manufacturer.contactNo ContactNumber, 
		   Food.foodID FoodID, Food.foodName FoodName, Food.expiryDate ExpiryDate, 
		   FoodDonationDetails.quantity AmountPerCategory, FoodDonationDetails.unitOfMeasure Measurement,
		   Food.foodType CategoryName
	FROM Manufacturer
	JOIN Food
	ON Manufacturer.manID = Food.manID
	JOIN FoodDonationDetails
	ON Food.foodID = FoodDonationDetails.foodID
	WHERE ( (CAST(Food.expiryDate AS DATETIME) - GETDATE()) < 0 ) --Compare expiryDate with current date...

GO
	PRINT 'View vw_PetsPerType created successfully...'
GO
--Calling the View with SELECT statement...
	SELECT * FROM vw_ExpiredFoodDetails
GO
--=========================================================================================

--vw_LowestFoods
--============================

IF EXISTS(SELECT Table_Name FROM INFORMATION_SCHEMA.VIEWS
		  WHERE Table_Name = 'vw_LowestFoods')
BEGIN
	DROP VIEW vw_LowestFoods
	PRINT 'View vw_LowestFoods is droped successfully...'
END
GO

CREATE VIEW vw_LowestFoods
AS

	SELECT TOP 3 Animal.animType CategoryName, SUM( Animal.stockLvl ) AS TotalAnimals
	FROM Animal
	GROUP BY Animal.animType, Animal.stockLvl --Included to avoid error...
	ORDER BY Animal.stockLvl ASC --Lowest to highest..

GO
	PRINT 'View vw_LowestFoods created successfully...'
GO
--Calling the View with SELECT statement...
	SELECT * FROM vw_LowestFoods
GO

--=========================================================================================
--VIEW CREATIONS DONE SUCCESSFULLY...
--=========================================================================================







