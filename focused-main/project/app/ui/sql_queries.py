

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
   `JobID` INTEGER PRIMARY KEY,
   `SchoolName` VARCHAR(255),
   `pictureDate` TIMESTAMP,
   `schoolLocation` VARCHAR(255),
   `schoolContactNumber` VARCHAR(255),
   `schoolEmail` VARCHAR(255),
   `schoolAddress` VARCHAR(255)
   ); """,      

   """CREATE TABLE `Students` (
   `StudentID` INTEGER PRIMARY KEY,
   `fname` VARCHAR(255),
   `lname` VARCHAR(255),
   `teacher` VARCHAR(255),
   `GradeOrClass` VARCHAR(255),
   `JobID` INTEGER,
   FOREIGN KEY (`JobID`) REFERENCES `Jobs` (`JobID`)
   ); """,

   """CREATE TABLE `ParentStudent` (
   `CustomerID` INTEGER,
   `StudentID` INTEGER,
   PRIMARY KEY (`CustomerID`, `StudentID`),
   FOREIGN KEY (`CustomerID`) REFERENCES `Customers` (`CustomerID`),
   FOREIGN KEY (`StudentID`) REFERENCES `Students` (`StudentID`)
   ); """,

   """CREATE TABLE `PriceSheets` (
   `PriceSheetID` INTEGER PRIMARY KEY,
   `ItemDescription` VARCHAR(255),
   `Price` DECIMAL,
   `SizeOrFormat` VARCHAR(255),
   `Discount` DECIMAL
   ); """,

   """CREATE TABLE `Orders` (
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
   ); """,

   """CREATE TABLE `Barcode` (
   `barcodeID` INTEGER PRIMARY KEY,
   `StudentID` INTEGER NOT NULL,
   `pictureCount` INTEGER DEFAULT 0,
   `picturePath` VARCHAR(255),
   FOREIGN KEY (`StudentID`) REFERENCES `Students` (`StudentID`)
   ); """]





test_data = [
   """INSERT INTO Photographers (PhotographerID, photographerfname, photographerlname, photographerContactNumber, photographerEmail) VALUES
   (1, 'John', 'Doe', '555-1234', 'john.doe@email.com'),
   (2, 'Jane', 'Smith', '555-5678', 'jane.smith@email.com'),
   (3, 'Sarah', 'Miller', '555-2020', 'sarah.miller@email.com'),
   (4, 'Michael', 'Davis', '555-3030', 'michael.davis@email.com'),
   (5, 'Emily', 'Taylor', '555-4040', 'emily.taylor@email.com');
   """,

   """INSERT INTO Customers (CustomerID, customerfname, customerlname, customerContactNumber, customerEmail, customerAddress) VALUES
   (1, 'Alice', 'Johnson', '555-9101', 'alice.johnson@email.com', '123 Apple St.'),
   (2, 'Bob', 'Williams', '555-1122', 'bob.williams@email.com', '456 Orange Ave.'),
   (3, 'Chris', 'Green', '555-1133', 'chris.green@email.com', '789 Banana Blvd.'),
   (4, 'Patricia', 'Lopez', '555-1144', 'patricia.lopez@email.com', '321 Cherry Pl.'),
   (5, 'David', 'Wilson', '555-1155', 'david.wilson@email.com', '654 Peach Terrace');
   """,

   """INSERT INTO Jobs (JobID, SchoolName, pictureDate, schoolLocation, schoolContactNumber, schoolEmail, schoolAddress) VALUES
   (1, 'Greenwood High', '2024-03-15 08:00:00', '789 Pine Rd.', '555-3131', 'info@greenwoodhigh.edu', '789 Pine Rd.'),
   (2, 'Sunnydale Elementary', '2024-04-20 08:00:00', '101 Maple Ln.', '555-3232', 'contact@sunnydaleelem.edu', '101 Maple Ln.'),
   (3, 'Riverside Middle', '2024-05-10 09:00:00', '234 Elm St.', '555-4242', 'admin@riversidemiddle.edu', '234 Elm St.'),
   (4, 'Hilltop High', '2024-06-05 08:30:00', '567 Cedar Ave.', '555-5353', 'info@hilltophigh.edu', '567 Cedar Ave.'),
   (5, 'Lakeside Elementary', '2024-07-15 08:00:00', '890 Birch Rd.', '555-6464', 'contact@lakesideelem.edu', '890 Birch Rd.');
   """,

   """INSERT INTO Students (StudentID, fname, lname, teacher, GradeOrClass, JobID) VALUES
   (3, 'Samantha', 'Morris', 'Mr. Gray', 'Grade 3', 3),
   (4, 'Noah', 'Jackson', 'Ms. Lee', 'Grade 5', 4),
   (5, 'Sophia', 'Garcia', 'Mrs. Hall', 'Grade 1', 5),
   (6, 'Daniel', 'Martinez', 'Mr. Smith', 'Grade 6', 3),
   (7, 'Isabella', 'Anderson', 'Ms. Johnson', 'Kindergarten', 5);
   """,

   """INSERT INTO ParentStudent (CustomerID, StudentID) VALUES
   (3, 3),
   (4, 4),
   (1, 5),
   (2, 6),
   (5, 7);
   """,

   """INSERT INTO PriceSheets (PriceSheetID, ItemDescription, Price, SizeOrFormat, Discount) VALUES
   (1, 'Standard Photo Package', 19.99, '8x10', 0.00),
   (2, 'Deluxe Photo Package', 29.99, '10x12', 5.00),
   (3, 'Economy Photo Package', 14.99, '5x7', 0.00),
   (4, 'School Yearbook Package', 24.99, '6x8', 2.00),
   (5, 'Premium Photo Package', 34.99, '12x15', 7.50);
   """,

   """INSERT INTO Orders (OrderID, CustomerID, JobID, PriceSheetID, items, DatePlaced, TotalAmount, Status) VALUES
   (3, 3, 3, 3, 1, '2024-05-03 09:00:00', 14.99, 'Processed'),
   (4, 4, 4, 4, 2, '2024-05-04 14:30:00', 47.98, 'Pending'),
   (5, 1, 5, 5, 3, '2024-05-05 16:00:00', 89.97, 'Shipped'),
   (6, 2, 3, 2, 2, '2024-05-06 10:00:00', 49.98, 'Delivered'),
   (7, 5, 5, 1, 4, '2024-05-07 11:15:00', 79.96, 'Pending');
   """,

   """INSERT INTO Barcode (barcodeID, StudentID, pictureCount, picturePath) VALUES
   (3, 3, 4, '/images/samantha_morris'),
   (4, 4, 5, '/images/noah_jackson'),
   (5, 5, 2, '/images/sophia_garcia'),
   (6, 6, 3, '/images/daniel_martinez'),
   (7, 7, 4, '/images/isabella_anderson'); """
]


select_photographers = """SELECT photographerfname, photographerlname, photographerContactNumber, photographerEmail 
                          FROM Photographers;"""

select_customers = """SELECT customerfname, customerlname, customerContactNumber, customerEmail, customerAddress 
                        FROM Customers;"""

select_jobs = """SELECT JobID, SchoolName, pictureDate, schoolLocation, schoolContactNumber, schoolEmail, schoolAddress 
                    FROM Jobs;"""

select_students_grades = """SELECT StudentID, fname, lname, teacher, GradeOrClass 
                            FROM Students 
                            WHERE GradeOrClass = 'Specific Grade/Class';"""

select_students_parents = """SELECT c.customerfname, c.customerlname, s.fname, s.lname 
                                FROM Customers c
                                JOIN ParentStudent ps ON c.CustomerID = ps.CustomerID
                                JOIN Students s ON ps.StudentID = s.StudentID;"""

select_orders = """SELECT OrderID, CustomerID, JobID, PriceSheetID, items, DatePlaced, TotalAmount, Status 
                                FROM Orders;"""

select_orders_by_customer = """SELECT OrderID, JobID, PriceSheetID, items, DatePlaced, TotalAmount, Status 
                                FROM Orders 
                                WHERE CustomerID = 'Specific Customer ID';"""

select_price_sheets = """SELECT ItemDescription, Price, SizeOrFormat, Discount 
                            FROM PriceSheets;"""

select_barcodes_students = """SELECT b.barcodeID, s.fname, s.lname, b.pictureCount, b.picturePath 
                                FROM Barcode b
                                JOIN Students s ON b.StudentID = s.StudentID;"""

select_orders_revenue = """SELECT COUNT(OrderID) AS TotalOrders, SUM(TotalAmount) AS TotalRevenue 
                            FROM Orders;"""

select_all_jobs_school = """SELECT SchoolName, schoolLocation, schoolContactNumber, schoolAddress, COUNT(*) AS Frequency
                              FROM Jobs
                              WHERE SchoolName = ?;"""


select_students_from_job_id = """SELECT Students.StudentID, Students.fname, Students.lname, Students.teacher, Students.GradeOrClass, Students.JobID
                                 FROM Students
                                 JOIN Jobs ON Students.JobID = Jobs.JobID
                                 WHERE Jobs.JobID = ?; """
