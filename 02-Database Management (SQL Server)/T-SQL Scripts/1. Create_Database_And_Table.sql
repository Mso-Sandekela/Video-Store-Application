--=========================================================================================
--Script file name: 1. Create_Database_And_Table.sql
--Name & Surname: Sopumelela Sandekela
--Student number: CON-1475940-C5L6
--Date: 18/11/2023
--Description: This file will created a Database and Tables for Tygervalley Pet Shelter (TPS)  
--=========================================================================================

USE master
GO 

--In case of re-runnig the script the database is droped...
IF EXISTS(SELECT name FROM master.dbo.sysdatabases 
WHERE name = 'TygerValleyPetShelter')
Begin
	DROP DATABASE TygerValleyPetShelter
	PRINT 'Tyger Valley Pet Shelter database is deleted...'
End
GO

--Code for creating TygerValleyPetShelter Database...
CREATE DATABASE TygerValleyPetShelter
ON PRIMARY
(

	NAME = 'TygerValleyPetShelter_Data',
	FILENAME = 'C:\SQL Server Project\TygerValleyPetShelter.mdf',
	SIZE = 5MB,
	FILEGROWTH = 10%

)
LOG ON
(

	NAME = 'TygerValleyPetShelter_Log',
	FILENAME = 'C:\SQL Server Project\TygerValleyPetShelter.ldf',
	SIZE = 5MB,
	FILEGROWTH = 10%

)
GO
PRINT 'Database TygerValleyPetShelter created successfully...'
PRINT ' '
GO


--Code for creating TygerValleyPetShelter Tables...
USE TygerValleyPetShelter --The database is called for use...
GO

CREATE TABLE Animal
(

	animID INT IDENTITY NOT NULL,
	animType VARCHAR(30) NOT NULL,
	animName VARCHAR (30) NOT NULL,
	stockLvl INT NOT NULL,
	CONSTRAINT animID_PK PRIMARY KEY (animID),
	CONSTRAINT CheckStockLvl CHECK (stockLvl >= 0)

)
GO
PRINT 'Table Animal created successfully...'
GO

--Creating table for Manufacturer...
CREATE TABLE Manufacturer
(

	manID INT IDENTITY NOT NULL,
	compName VARCHAR (30) NOT NULL,
	contactNo VARCHAR (15) NOT NULL,
	emailAddress VARCHAR (30) NULL,
	CONSTRAINT manID_PK PRIMARY KEY(manID)

)
GO
PRINT 'Table Manufacturer created successfully...'
GO


--Creating Table for Food...
CREATE TABLE Food
(

	foodID INT IDENTITY NOT NULL,
	foodType VARCHAR(30) NOT NULL,
	foodName VARCHAR(30) NOT NULL,
	expiryDate DATE NOT NULL,
	manID INT NOT NULL
	CONSTRAINT foodID_PK PRIMARY KEY(foodID),
	CONSTRAINT manID_FK FOREIGN KEY(manID) REFERENCES Manufacturer(manID),
	CONSTRAINT CheckExpiryDate CHECK (expiryDate > (GETDATE()))

)
GO
	PRINT 'Table Food created successfully...' 
GO


CREATE TABLE FoodDonationDetails
(
	animID INT NOT NULL,
	foodID INT NOT NULL,
	quantity FLOAT NOT NULL,
	unitOfMeasure VARCHAR (15) NOT NULL,
	PRIMARY KEY (animID, foodID), --Composite keys of the Intersect table... 
	CONSTRAINT animID_FK FOREIGN KEY (animID) REFERENCES Animal(animID),
	CONSTRAINT foodID_FK FOREIGN KEY (foodID) REFERENCES Food(foodID),
	CONSTRAINT CheckQuantity CHECK (quantity >= 0)

)
 GO
 PRINT 'Table FoodDonationDetails created successfully...'
GO

--=========================================================================================
--SCRIPT COMPLETE...
--=========================================================================================





