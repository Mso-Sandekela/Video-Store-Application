--=========================================================================================
--Script file name: 2. Sample_Data_Insert.sql
--Name & Surname: Sopumelela Sandekela
--Student number: CON-1475940-C5L6
--Date: 20/11/2023
--Description: This file will Insert sample data on Tables that exist on Tygervalley Pet Shelter (TPS) database.  
--=========================================================================================

USE TygerValleyPetShelter --The Databse is called for use in order to insert values...
GO


--INSERT is used to insert values into Animal table...
INSERT INTO Animal(animType, animName, stockLvl)
VALUES ('Mammal','Dog', 20), ('Bird', 'Chicken', 2368),('Bird','Cockatoo', 54), ('Bird','Parakeets', 32),
	   ('Mammal','Sheep', 386), ('Mammal','Goat', 142), ( 'Bird', 'Dove', 82), ('Mammal','Cow', 431),
	   ('Bird','Parrotlet', 72), ('Bird','Hyacinth',44), ('Mammal','Pig', 31),
	   ('Mammal','Horse', 47), ( 'Mammal', 'Cat',24), ( 'Bird','Eclectus', 65)
GO
  PRINT 'Inserted values successfully on table Animal...'
GO


--Insert values for the Manufacturer table...
INSERT INTO Manufacturer(compName, contactNo, emailAddress)
VALUES ('Animal Feed Store', '073 054 4845', 'AnimalFeed@gmail.com'),
	   ('Pet Your Pet Store', '083 543 6632', 'PetUrPet@Outlook.com' ),
	   ('We Care For Pets', '060 879 5452', NULL),
	   ('Green Feeds', '073 440 9845', 'GreenFeeds@green.net' ),
	   ('Leaves And Seeds', '063 720 9932', NULL ),
	   ('Feed For Pet', '083 994 5589', NULL),
	   ('Corner Store', '060 389 0348', 'CornerStore@gmail.com')
GO
  PRINT 'Inserted values successfully on table Manufacturer...'
GO


--Insert values for the Manufacturer table...
ALTER TABLE Food NOCHECK CONSTRAINT [CheckExpiryDate]--Disable Check Constraint to allow sample data 
													 --I will need in future on the project...
INSERT INTO Food(foodType, foodName, expiryDate, manID)
VALUES ('Seed', 'Sunflower Seeds', 'Feb 14 2024', 2),
	   ('Seed', 'Pumpkin seeds', 'Jan 03 2026', 6),
	   ('Vegatable', 'Broccoli', 'Apr 23 2024', 1),
	   ('Seed', 'Hemp Seeds', 'Nov 09 2022', 3),
	   ('Vegatable', 'Carrots', 'May 17 2022', 4),
	   ('Vegatable', 'Green Beans', 'Feb 28 2024', 7),
	   ('Vegatable', 'Spinach', 'May 17 2024', 5),
	   ('Seed', 'Maze', 'Jan 25 2022', 6),
	   ('Seed', 'Blackseed', 'Nov 11 2025', 3),
	   ('Vegatable', 'Mixed Veg', 'Sep 04 2024', 1),
	   ('Seed', 'Croton flavens', 'Oct 01 2025', 6),
	   ('Vegatable', 'Cabage', 'Dec 27 2022', 7),
	   ('Seed', 'Breek Mielies', 'Apr 02 2022', 6),
	   ('Seed', 'Budgie seed', 'Jan 01 2022', 6),
	   ('Seed', 'White proso millet', 'May 06 2025', 2),
	   ('Seed', 'shelled corn', 'Jun 23 2022', 6),
	   ('Vegatable', 'Forage', 'Feb 28 2025', 5),
	   ('Seed', 'Peanuts', 'Nov 09 2022', 2),
	   ('Vegatable', 'Grass', 'May 21 2022', 7),
	   ('Seed', 'Soybean', 'Dec 03 2025', 3)

GO
  PRINT 'Inserted values successfully on table Food...'
GO


--The Values of the FOREIGN KEYS Need to be existing values...
INSERT INTO FoodDonationDetails(quantity, unitOfMeasure, animID, foodID) 
VALUES (22.65, 'Kilograms', 6, 5),
	   (4374.00, 'Grams', 13, 3),
	   (2069.43, 'Grams', 1, 6),
	   (54.78, 'Kilograms', 11, 5),
	   (78.65, 'Kilograms', 8, 7),
	   (7588.35, 'Grams', 6, 3),
	   (17.52, 'Kilograms', 9, 2),
	   (213.21, 'Grams', 9, 20),
	   (500.04, 'Grams', 10, 14),
	   (349.98, 'Grams', 14, 16),
	   (21.88, 'Kilograms', 6, 12),
	   (54.99, 'Kilograms', 12, 19),
	   (110.52, 'Kilograms', 8, 12),
	   (17.52, 'Kilograms', 1, 10)
GO
  PRINT 'Inserted values successfully on table FoodDonationDetails...'
GO

--=========================================================================================
--INSERTING DATA COMPLETED SUCCESSFULLY...
--=========================================================================================