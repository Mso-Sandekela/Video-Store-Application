--=========================================================================================
--Script file name: 8. Create_Trigger.sql
--Name & Surname: Sopumelela Sandekela
--Student number: CON-1475940-C5L6
--Date: 24/11/2023
--Description: This file will create two triggers on the tables that I have created.
--=========================================================================================

--[AFTER INSERT] TRIGGER
--============================

USE TygerValleyPetShelter --Call database for use...
GO

--Creating FIRST(1st) TRIGGER For Manufacturer...
CREATE TRIGGER tr_Manufacturer
ON Manufacturer
AFTER INSERT --After deleting the following message will appear... 
AS
	PRINT 'New manufacturering company has been added.'
GO
PRINT '[AFTER INSERT-TRIGGER] tr_Manufacturer have be created successfully...'
GO

--Testin TRIGGER...
INSERT INTO Manufacturer (compName, contactNo, emailAddress)
Values ('FRESH LINE MASTERES', '073 674 3582', 'FLineMasteres@gmail.com')
GO
--==========================================================================

--[INSTEAD OF DELETE] TRIGGER
--============================

--Creating SECOND(2nd) TRIGGER...
CREATE TRIGGER tr_FoodDonationDetails
ON FoodDonationDetails
INSTEAD OF DELETE --Instead of deleting the following message will be displayed...
AS
	PRINT 'Can not delete record(s) on FoodDonationDetails as it affects tables based on it.'
GO

--Testing TRIGGER...
DELETE 
FROM FoodDonationDetails
WHERE (quantity > 23)
GO
PRINT '[INSTEAD OF DELETE-TRIGGER] tr_FoodDonationDetails have be created successfully...'
GO
--==========================================================================

