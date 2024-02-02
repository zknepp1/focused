CREATE TABLE `Photographers` (
  `PhotographerID` INTEGER PRIMARY KEY,
  `photographerfname` VARCHAR(255),
  `photographerlname` VARCHAR(255),
  `photographerContactNumber` VARCHAR(255),
  `photographerEmail` VARCHAR(255)
);

CREATE TABLE `Customers` (
  `CustomerID` INTEGER PRIMARY KEY,
  `customerfname` VARCHAR(255),
  `customerlname` VARCHAR(255),
  `customerContactNumber` VARCHAR(255),
  `customerEmail` VARCHAR(255),
  `customerAddress` VARCHAR(255)
);

CREATE TABLE `Jobs` (
  `JobID` INTEGER PRIMARY KEY,
  `SchoolName` VARCHAR(255),
  `pictureDate` TIMESTAMP,
  `schoolLocation` VARCHAR(255),
  `schoolContactNumber` VARCHAR(255),
  `schoolEmail` VARCHAR(255),
  `schoolAddress` VARCHAR(255)
);

CREATE TABLE `Students` (
  `StudentID` INTEGER PRIMARY KEY,
  `fname` VARCHAR(255),
  `lname` VARCHAR(255),
  `teacher` VARCHAR(255),
  `GradeOrClass` VARCHAR(255),
  `JobID` INTEGER,
  FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`)
);

CREATE TABLE `ParentStudent` (
  `CustomerID` INTEGER,
  `StudentID` INTEGER,
  PRIMARY KEY (`CustomerID`, `StudentID`),
  FOREIGN KEY (`CustomerID`) REFERENCES `Customers` (`CustomerID`),
  FOREIGN KEY (`StudentID`) REFERENCES `Students` (`StudentID`)
);

CREATE TABLE `PriceSheets` (
  `PriceSheetID` INTEGER PRIMARY KEY,
  `ItemDescription` VARCHAR(255),
  `Price` DECIMAL,
  `SizeOrFormat` VARCHAR(255),
  `Discount` DECIMAL
);

CREATE TABLE `Orders` (
  `OrderID` INTEGER PRIMARY KEY,
  `CustomerID` INTEGER,
  `JobID` INTEGER,
  `PriceSheetID` INTEGER,
  `items` INTEGER,
  `DatePlaced` TIMESTAMP,
  `TotalAmount` DECIMAL,
  `Status` VARCHAR(255),
  FOREIGN KEY (`CustomerID`) REFERENCES `Customers` (`CustomerID`),
  FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`),
  FOREIGN KEY (`PriceSheetID`) REFERENCES `PriceSheets` (`PriceSheetID`)
);

CREATE TABLE `Barcode` (
  `barcodeID` INTEGER PRIMARY KEY,
  `StudentID` INTEGER,
  `pictures` INTEGER,
  FOREIGN KEY (`StudentID`) REFERENCES `Students` (`StudentID`)
);
