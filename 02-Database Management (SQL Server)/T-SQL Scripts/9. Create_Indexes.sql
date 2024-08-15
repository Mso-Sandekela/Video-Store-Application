--=========================================================================================
--Script file name: 9. Create_Indexes.sql
--Name & Surname: Sopumelela Sandekela
--Student number: CON-1475940-C5L6
--Date: 25/11/2023
--Description: This file will Create Indexes on the tables I have created.
--=========================================================================================

--[CREATING INDEXES]

USE TygerValleyPetShelter
GO

--Nonclustered Index on Animal Table...
CREATE INDEX idx_Animal
ON Animal
(
	animName
)
GO
PRINT 'Nonclustered Index created successfully on table Animal...'
GO

--Nonclustered Index on Food Table...
CREATE INDEX idx_Food
ON Food
(
	foodName
)
GO
PRINT 'Nonclustered Index created successfully on table Food...'
GO

--Nonclustered Index on Manufacturer Table...
CREATE INDEX idx_Manufacturer
ON Manufacturer
(
	compName
)
GO
PRINT 'Nonclustered Index created successfully on table Manufacturer...'
GO

--=========================================================================================
--CREATING INDEXES COMPLETED SUCCESSFULLY...
--=========================================================================================


