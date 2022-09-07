/*
 * 596. Classes More Than 5 Students
 * 🟢 Easy
 *
 * https://leetcode.com/problems/classes-more-than-5-students/
 *
 * Tags: Database
 * 
 * Group the students' records by class, return the class names for classes
 * that have 5 students or more.
 */
SELECT `class` from `Courses` group by `class` having count(*) > 4;
