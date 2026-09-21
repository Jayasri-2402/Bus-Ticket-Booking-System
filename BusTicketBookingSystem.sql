CREATE DATABASE bus_ticket_booking;
USE bus_ticket_booking;
CREATE TABLE customer(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
contact_no VARCHAR(10),
age INT,
gender VARCHAR(50),
journey_date DATE
)
SELECT*FROM customer;
DROP TABLE customer;

CREATE TABLE busdetails(
customer_id INT,
bus_id INT,
bus_name VARCHAR(40),
destination VARCHAR(40),
booking_id INT,
departure_time VARCHAR(10)
)
SELECT*FROM busdetails;
DROP TABLE busdetails;

CREATE TABLE booking(
customer_id INT,
ticket_count INT,
total_amount DECIMAL(10,2),
ext_cost DECIMAL(10,2)
)
SELECT*FROM booking;

SELECT*FROM customer
WHERE customer_id=1001;

TRUNCATE TABLE customer;

SELECT c.customer_id,c.customer_name,c.journey_date,b.bus_id,b.bus_name,b.destination,b.booking_id,b.departure_time,bk.ticket_count,bk.total_amount,bk.ext_cost FROM customer as c INNER JOIN busdetails as b ON c.customer_id=b.customer_id INNER JOIN booking as bk ON c.customer_id=bk.customer_id;







