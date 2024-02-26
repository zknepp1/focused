

# Create a table
create_database = [
   """CREATE TABLE `Photographers` (
   `PhotographerID` INTEGER PRIMARY KEY,
   `photographerfname` VARCHAR(255),
   `photographerlname` VARCHAR(255),
   `photographerContactNumber` VARCHAR(255),
   `photographerEmail` VARCHAR(255)
   );""",

   """CREATE TABLE `Customers` (
   `CustomerID` INTEGER PRIMARY KEY,
   `customerfname` VARCHAR(255),
   `customerlname` VARCHAR(255),
   `customerContactNumber` VARCHAR(255),
   `customerEmail` VARCHAR(255),
   `customerAddress` VARCHAR(255)
   );""",

   """CREATE TABLE `Jobs` (
  `JobID` integer PRIMARY KEY,
  `Title` varchar(255),
  `Sync` varchar(255),
  `numImages` integer,
  `jobType` varchar(255),
  `marketingCampaign` varchar(255),
  `priceSheet` varchar(255),
  `keyword` varchar(255),
  `jobDate` timestamp,
  `createDate` timestamp,
  `lastModified` timestamp,
  `jobLocation` varchar(255),
  `jobContactNumber` varchar(255),
  `jobEmail` varchar(255),
  `jobAddress` varchar(255)
   ); """,      

   """CREATE TABLE `Students` (
  `StudentID` integer PRIMARY KEY,
  `fname` varchar(255),
  `lname` varchar(255),
  `teacher` varchar(255),
  `GradeOrClass` varchar(255),
  `barcodeID` integer,
  `JobID` integer
   );""",

   """CREATE TABLE `ParentStudent` (
   `CustomerID` INTEGER,
   `StudentID` INTEGER,
   PRIMARY KEY (`CustomerID`, `StudentID`),
   FOREIGN KEY (`CustomerID`) REFERENCES `Customers` (`CustomerID`),
   FOREIGN KEY (`StudentID`) REFERENCES `Students` (`StudentID`)
   ); """,

   """CREATE TABLE `PriceSheets` (
  `PriceSheetID` integer PRIMARY KEY,
  `Description` varchar(255),
  `Sync` integer,
  `greenScreen` varchar(255),
  `jobCount` integer,
  `lastModified` timestamp,
  `SizeOrFormat` integer,
  `Discount` integer
   ); """,

   """CREATE TABLE `Orders` (
  `OrderID` integer PRIMARY KEY,
  `DatePlaced` timestamp,
  `CustomerID` integer,
  `lName` varchar(255),
  `fName` varchar(255),
  `JobID` integer,
  `Job` varchar(255),
  `releaseDate` timestamp,
  `Total` integer,
  `paymentStatus` varchar(255),
  `paymentDate` timestamp,
  `subTotal` integer,
  `Shipping` integer,
  `Handling` integer,
  `Tax` integer,
  `Discount` integer,
  `netPay` integer,
  `PriceSheetID` integer,
  `items` integer
   ); """,

   """CREATE TABLE `Barcode` (
   `barcodeID` INTEGER PRIMARY KEY,
   `StudentID` INTEGER NOT NULL,
   `pictureCount` INTEGER DEFAULT 0,
   `picturePath` VARCHAR(255),
   FOREIGN KEY (`StudentID`) REFERENCES `Students` (`StudentID`)
   ); """,

   "ALTER TABLE `Orders` ADD FOREIGN KEY (`CustomerID`) REFERENCES `Customers` (`CustomerID`);",
   "ALTER TABLE `Orders` ADD FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`);",
   "ALTER TABLE `Orders` ADD FOREIGN KEY (`PriceSheetID`) REFERENCES `PriceSheets` (`PriceSheetID`);",
   "ALTER TABLE `Students` ADD FOREIGN KEY (`barcodeID`) REFERENCES `Barcode` (`barcodeID`);",
   "ALTER TABLE `Photographers` ADD FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`);",
   "ALTER TABLE `Students` ADD FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`);",
   "ALTER TABLE `Students` ADD FOREIGN KEY (`StudentID`) REFERENCES `Customers` (`StudentID`);"]



delete_database = [
    "DROP TABLE IF EXISTS Photographers;",
    "DROP TABLE IF EXISTS Customers;",
    "DROP TABLE IF EXISTS Jobs;",
    "DROP TABLE IF EXISTS Students;",
    "DROP TABLE IF EXISTS ParentStudent;",
    "DROP TABLE IF EXISTS PriceSheets;",
    "DROP TABLE IF EXISTS Orders;",
    "DROP TABLE IF EXISTS Barcode;"
]





select_photographers = """SELECT photographerfname, photographerlname, photographerContactNumber, photographerEmail 
                          FROM Photographers;"""

select_customers = """SELECT customerfname, customerlname, customerContactNumber, customerEmail, customerAddress 
                        FROM Customers;"""

select_jobs = """SELECT JobID, Title, jobDate, jobLocation, jobContactNumber, jobEmail, jobAddress 
                    FROM Jobs;"""


select_students_grades = """SELECT StudentID, fname, lname, teacher, GradeOrClass 
                            FROM Students 
                            WHERE GradeOrClass = 'Specific Grade/Class';"""

select_students_parents = """SELECT c.customerfname, c.customerlname, s.fname, s.lname 
                                FROM Customers c
                                JOIN ParentStudent ps ON c.CustomerID = ps.CustomerID
                                JOIN Students s ON ps.StudentID = s.StudentID;"""


select_orders = """SELECT OrderID, CustomerID, JobID, PriceSheetID, items, DatePlaced, Total, paymentStatus 
                                FROM Orders;"""

select_orders_by_customer = """SELECT OrderID, JobID, PriceSheetID, items, DatePlaced, Total, paymentStatus 
                                FROM Orders 
                                WHERE CustomerID = 'Specific Customer ID';"""


select_price_sheets = """SELECT PriceSheetID, Description, Sync, greenScreen, Discount 
                            FROM PriceSheets;"""

select_barcodes_students = """SELECT b.barcodeID, s.fname, s.lname, b.pictureCount, b.picturePath 
                                FROM Barcode b
                                JOIN Students s ON b.StudentID = s.StudentID;"""

select_orders_revenue = """SELECT COUNT(OrderID) AS TotalOrders, SUM(TotalAmount) AS TotalRevenue 
                            FROM Orders;"""

select_all_jobs_school = """SELECT Title, jobLocation, jobContactNumber, jobAddress, COUNT(*) AS Frequency
                              FROM Jobs
                              WHERE SchoolName = ?;"""


select_students_from_job_id = """SELECT Students.StudentID, Students.fname, Students.lname, Students.teacher, Students.GradeOrClass, Students.JobID
                                 FROM Students
                                 JOIN Jobs ON Students.JobID = Jobs.JobID
                                 WHERE Jobs.JobID = ?; """

