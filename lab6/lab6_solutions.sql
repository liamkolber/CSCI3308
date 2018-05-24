/*Liam Kolber and Evan Dorrough*/
/*1*/
SELECT * FROM store ORDER BY sname;
/*1*/
SELECT * FROM store ORDER BY sname LIMIT 3;
/*3*/
SELECT * FROM (SELECT * FROM store ORDER BY sname DESC LIMIT 3) t ORDER BY sname; 
/*4*/
SELECT * FROM store WHERE price > 1;
/*5*/
SELECT *, price*qty AS total FROM store;
/*6*/
SELECT sum(price*qty) FROM store;
/*7*/
SELECT COUNT(DISTINCT(sname)) FROM store;

/*8*/
SELECT cname FROM course WHERE department_id = (SELECT id FROM department WHERE name = 'CSC');
/*9*/
SELECT sum(count) FROM enrollment;
/*10*/
SELECT COUNT(DISTINCT(cname)) FROM course;
/*11*/
SELECT COUNT(DISTINCT(name)) FROM department;
/*12*/
SELECT CONCAT(department.name, course.cname) AS coursename FROM department, course WHERE department.name = 'CSC';
/*13*/
SELECT CONCAT(department.name, ' ', course.cname) AS coursename FROM department, course WHERE department.id = course.department_id;
/*14*/
SELECT department.name, course.cname, enrollment.count FROM department, course, enrollment WHERE department.id = course.department_id AND enrollment.id = course.id;

