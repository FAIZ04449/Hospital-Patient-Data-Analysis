CREATE DATABASE hospital_db;
USE hospital_db;
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    disease VARCHAR(50),
    doctor VARCHAR(50),
    treatment_cost INT
);
INSERT INTO patients VALUES
(1,45,'Male','Diabetes','Dr Shah',5000),
(2,30,'Female','Fever','Dr Patil',2000),
(3,55,'Male','Heart Disease','Dr Shah',20000),
(4,22,'Female','Flu','Dr Kulkarni',1500),
(5,40,'Male','Diabetes','Dr Shah',4500),
(6,60,'Female','Heart Disease','Dr Patil',22000),
(7,35,'Male','Fever','Dr Kulkarni',1800),
(8,28,'Female','Flu','Dr Shah',1600),
(9,50,'Male','Diabetes','Dr Patil',5200),
(10,33,'Female','Fever','Dr Shah',2100);

SELECT * FROM patients;

SELECT disease, COUNT(*) AS patient_count
FROM patients
GROUP BY disease;

SELECT AVG(treatment_cost) AS avg_cost
FROM patients;

SELECT doctor, COUNT(*) AS total_patients
FROM patients
GROUP BY doctor
ORDER BY total_patients DESC
LIMIT 1;