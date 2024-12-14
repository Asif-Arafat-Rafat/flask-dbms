-- Create the projectcourses table
CREATE TABLE projectcourses (
    course_id INT PRIMARY KEY,
    course_title VARCHAR2(50),
    year INT,
    semester INT
);


CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR2(200),
    course_id INT,
    submission_status NUMBER(1) DEFAULT 0, 
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (course_id) REFERENCES projectcourses(course_id) 
    ON DELETE CASCADE
);

CREATE TABLE project_groups (
    group_id NUMBER PRIMARY KEY,
    group_member INT,
    project_id INT,
    FOREIGN KEY (project_id) REFERENCES projects (project_id) 
    ON DELETE CASCADE
);

CREATE TABLE member (
    group_id INT,
    roll INT,
    FOREIGN KEY (group_id) REFERENCES project_groups (group_id)
);



-- Insert data into projectcourses table
INSERT INTO projectcourses (course_id, course_title, year, semester) 
VALUES (3200, 'Electronic Project Design and Development', 3, 2);

INSERT INTO projectcourses (course_id, course_title, year, semester) 
VALUES (3210, 'Database System Lab Project', 3, 2);

INSERT INTO projectcourses (course_id, course_title, year, semester) 
VALUES (3204, 'DSP Lab Project', 3, 2);

INSERT INTO projectcourses (course_id, course_title, year, semester) 
VALUES (3100, 'Internet Programming Lab Project', 3, 1);

INSERT INTO projectcourses (course_id, course_title, year, semester) 
VALUES (3102, 'Industrial Electronics Lab Project', 3, 1);


ALTER TABLE projectcourses
ADD credit NUMBER(3, 2);

UPDATE projectcourses SET credit = 1.5 WHERE course_id = 3100;
UPDATE projectcourses SET credit = 0.75 WHERE course_id = 3102;
UPDATE projectcourses SET credit = 1.5 WHERE course_id = 3200;
UPDATE projectcourses SET credit = 0.75 WHERE course_id = 3204;
UPDATE projectcourses SET credit = 0.75 WHERE course_id = 3210;

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (1, 'Vaccine Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (2, 'Farmer Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (3, 'Day Care Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (4, 'Flight Booking & Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (5, 'Attendance Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (6, 'Electricity Bill Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (7, 'Pet Shop Management', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (8, 'Retail Shop Management', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (9, 'Medical Supply Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (10, 'Event Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (11, 'Makeup Store Management', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (12, 'Course Training Management', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (13, 'Employee Payroll System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (14, 'Home Renting Database Management Project', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (15, 'Insurance Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (16, 'Real Estate Listings Management', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (17, 'House Rental Management', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (18, 'Student Result Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (19, 'Home Appliances Shop Management', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));

INSERT INTO projects (project_id, project_name, course_id, submission_status, start_date, end_date)
VALUES (20, 'Gym Management System', 3210, 0, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-04', 'YYYY-MM-DD'));


INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (1, 1, 1);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (2, 1, 2);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (3, 1, 3);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (4, 1, 4);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (5, 1, 5);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (6, 1, 6);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (7, 1, 7);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (8, 1, 8);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (9, 1, 9);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (10, 1, 10);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (11, 1, 11);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (12, 1, 12);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (13, 1, 13);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (14, 1, 14);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (15, 1, 15);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (16, 1, 16);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (17, 1, 17);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (18, 1, 18);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (19, 1, 19);

INSERT INTO project_groups (group_id, group_member, project_id) 
VALUES (20, 1, 20);


INSERT INTO member (group_id, roll) 
VALUES (1, 2009003);

INSERT INTO member (group_id, roll) 
VALUES (2, 2009004);

INSERT INTO member (group_id, roll) 
VALUES (3, 2009005);

INSERT INTO member (group_id, roll) 
VALUES (4, 2009008);

INSERT INTO member (group_id, roll) 
VALUES (5, 2009009);

INSERT INTO member (group_id, roll) 
VALUES (6, 2009010);

INSERT INTO member (group_id, roll) 
VALUES (7, 2009011);

INSERT INTO member (group_id, roll) 
VALUES (8, 2009013);

INSERT INTO member (group_id, roll) 
VALUES (9, 2009015);

INSERT INTO member (group_id, roll) 
VALUES (10, 2009017);

INSERT INTO member (group_id, roll) 
VALUES (11, 2009018);

INSERT INTO member (group_id, roll) 
VALUES (12, 2009019);

INSERT INTO member (group_id, roll) 
VALUES (13, 2009022);

INSERT INTO member (group_id, roll) 
VALUES (14, 2009024);

INSERT INTO member (group_id, roll) 
VALUES (15, 2009025);

INSERT INTO member (group_id, roll) 
VALUES (16, 2009027);

INSERT INTO member (group_id, roll) 
VALUES (17, 2009030);

INSERT INTO member (group_id, roll) 
VALUES (18, 2009031);

INSERT INTO member (group_id, roll) 
VALUES (19, 2009032);

INSERT INTO member (group_id, roll) 
VALUES (20, 2009033);


INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (21, 'Fire and gas leak detection and automatic prevention system', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (22, 'Arduino based fire detection and Alert system', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (23, 'Smart Car Parking System using Arduino', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (24, 'Surveillance/Spy car with 180° camera control', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (25, 'Smart home automation system', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (26, 'Arduino based Smart Vacuum Cleaner', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (27, 'RFID based Smart parking system', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (28, 'Radar missile system using Arduino', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (29, 'Baby Monitoring System Using Wireless Sensor Networks', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (30, 'Gesture Device For Bed Lying Person And Health Monitoring System', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (31, 'SignSpeak: Real-Time Sign Language Recognition and Translation', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (32, 'Surveying the upstream flow level to prevent flood damage using wireless technology', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (33, 'Ultrasonic Radar System', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (34, 'Fingerprint Based Electronic Voting Machine (EVM)', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (35, 'Intelligent Video Surveillance System', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (36, 'SenseStick: A Comprehensive Navigational Aid with Safety Features for Elderly and Visually Impaired Individuals', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (37, 'Smart Vacuum Cleaning Robot', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (38, 'Female security alert and tracking system', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (39, 'Traffic signal management and control system based on density of vehicles and emergency vehicles', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (40, 'IoT Controlled Fire Fighting Robot with Arduino', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (41, 'Green house monitoring and control system', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (42, 'Automatic Solar tracker', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (43, 'IoT-based Remote Health Monitoring System with Vital Sign Alerts for At-risk Patients utilizing ML', 3200, DATE '2024-11-01', DATE '2025-03-01', 0);

-- Insert new projects into the projects table starting from project_id 44
INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (44, 'Fire extinguisher using sound wave', 3204, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-06', 'YYYY-MM-DD'), 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (45, 'Digital Stethoscope using Arduino sensors', 3200, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-06', 'YYYY-MM-DD'), 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (46, 'Bluetooth controlled environment monitoring Vehicle', 3200, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-06', 'YYYY-MM-DD'), 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (47, 'Pen Plotter', 3210, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-06', 'YYYY-MM-DD'), 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (48, 'Eye-Tracking System for Disability Assistance', 3210, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-06', 'YYYY-MM-DD'), 0);

INSERT INTO projects (project_id, project_name, course_id, start_date, end_date, submission_status)
VALUES (49, 'Smart home automation system with speech recognition', 3100, TO_DATE('2024-11-06', 'YYYY-MM-DD'), TO_DATE('2024-12-06', 'YYYY-MM-DD'), 0);


-- Inserting groups for each project (each group has two members)
INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (21, 21, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (22, 22, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (23, 23, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (24, 24, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (25, 25, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (26, 26, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (27, 27, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (28, 28, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (29, 29, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (30, 30, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (31, 31, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (32, 32, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (33, 33, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (34, 34, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (35, 35, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (36, 36, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (37, 37, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (38, 38, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (39, 39, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (40, 40, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (41, 41, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (42, 42, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (43, 43, 2);


-- Assigning members (roll numbers) to each group, where roll numbers are adjacent
-- Group 21
INSERT INTO member (group_id, roll) VALUES (21, 2009001);
INSERT INTO member (group_id, roll) VALUES (21, 2009002);

-- Group 22
INSERT INTO member (group_id, roll) VALUES (22, 2009003);
INSERT INTO member (group_id, roll) VALUES (22, 2009034);

-- Group 23
INSERT INTO member (group_id, roll) VALUES (23, 2009004);
INSERT INTO member (group_id, roll) VALUES (23, 2009010);

-- Group 24
INSERT INTO member (group_id, roll) VALUES (24, 2009005);
INSERT INTO member (group_id, roll) VALUES (24, 2009031);

-- Group 25
INSERT INTO member (group_id, roll) VALUES (25, 2009006);
INSERT INTO member (group_id, roll) VALUES (25, 2009027);

-- Group 26
INSERT INTO member (group_id, roll) VALUES (26, 2009008);
INSERT INTO member (group_id, roll) VALUES (26, 2009024);

-- Group 27
INSERT INTO member (group_id, roll) VALUES (27, 2009009);
INSERT INTO member (group_id, roll) VALUES (27, 2009046);

-- Group 28
INSERT INTO member (group_id, roll) VALUES (28, 2009011);
INSERT INTO member (group_id, roll) VALUES (28, 2009017);

-- Group 29
INSERT INTO member (group_id, roll) VALUES (29, 2009013);
INSERT INTO member (group_id, roll) VALUES (29, 2009059);

-- Group 30
INSERT INTO member (group_id, roll) VALUES (30, 2009014);
INSERT INTO member (group_id, roll) VALUES (30, 2009023);

-- Group 31
INSERT INTO member (group_id, roll) VALUES (31, 2009015);
INSERT INTO member (group_id, roll) VALUES (31, 2009016);

-- Group 32
INSERT INTO member (group_id, roll) VALUES (32, 2009018);
INSERT INTO member (group_id, roll) VALUES (32, 2009053);

-- Group 33
INSERT INTO member (group_id, roll) VALUES (33, 2009019);
INSERT INTO member (group_id, roll) VALUES (33, 2009026);

-- Group 34
INSERT INTO member (group_id, roll) VALUES (34, 2009020);
INSERT INTO member (group_id, roll) VALUES (34, 1809009);

-- Group 35
INSERT INTO member (group_id, roll) VALUES (35, 2009022);
INSERT INTO member (group_id, roll) VALUES (35, 2009025);

-- Group 36
INSERT INTO member (group_id, roll) VALUES (36, 2009028);
INSERT INTO member (group_id, roll) VALUES (36, 2009057);

-- Group 37
INSERT INTO member (group_id, roll) VALUES (37, 2009029);
INSERT INTO member (group_id, roll) VALUES (37, 2009033);

-- Group 38
INSERT INTO member (group_id, roll) VALUES (38, 2009030);
INSERT INTO member (group_id, roll) VALUES (38, 2009036);

-- Group 39
INSERT INTO member (group_id, roll) VALUES (39, 2009032);
INSERT INTO member (group_id, roll) VALUES (39, 2009035);

-- Group 40
INSERT INTO member (group_id, roll) VALUES (40, 2009037);
INSERT INTO member (group_id, roll) VALUES (40, 2009047);

-- Group 41
INSERT INTO member (group_id, roll) VALUES (41, 2009038);
INSERT INTO member (group_id, roll) VALUES (41, 2009040);

-- Group 42
INSERT INTO member (group_id, roll) VALUES (42, 2009041);
INSERT INTO member (group_id, roll) VALUES (42, 1909019);

-- Group 43
INSERT INTO member (group_id, roll) VALUES (42, 2009042);
INSERT INTO member (group_id, roll) VALUES (42, 2009049);


INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (44, 44, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (45, 45, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (46, 46, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (47, 47, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (48, 48, 2);

INSERT INTO project_groups (group_id, project_id, group_member)
VALUES (49, 49, 2);


INSERT INTO member (group_id, roll) VALUES (44, 2009043);
INSERT INTO member (group_id, roll) VALUES (44, 2009044);

INSERT INTO member (group_id, roll) VALUES (45, 2009045);
INSERT INTO member (group_id, roll) VALUES (45, 2009056);


INSERT INTO member (group_id, roll) VALUES (46, 2009048);
INSERT INTO member (group_id, roll) VALUES (46, 2009050);


INSERT INTO member (group_id, roll) VALUES (47, 2009051);
INSERT INTO member (group_id, roll) VALUES (47, 2009052);


INSERT INTO member (group_id, roll) VALUES (48, 2009054);
INSERT INTO member (group_id, roll) VALUES (48, 2009060);


INSERT INTO member (group_id, roll) VALUES (49, 2009055);
INSERT INTO member (group_id, roll) VALUES (49, 2009058);