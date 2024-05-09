# MySQL Advanced

This repository contains SQL scripts for advanced MySQL concepts. The scripts are organized into tasks, each addressing specific requirements and objectives.

## Table of Contents

1. [Introduction](#introduction)
2. [Tasks](#tasks)
3. [Usage](#usage)
4. [Resources](#resources)
5. [Credits](#credits)

## Introduction

This project focuses on advanced SQL concepts in MySQL. It covers topics such as creating tables with constraints, optimizing queries with indexes, implementing stored procedures, functions, views, and triggers.

## Tasks

1. **We are all unique!**
   - Create a table `users` with specific attributes.
   
2. **In and not out**
   - Create a table `users` with additional requirements including enumerations.
   
3. **Best band ever!**
   - Rank country origins of bands based on the number of fans.
   
4. **Old school band**
   - List bands with Glam rock as their main style, ranked by their longevity.
   
5. **Buy buy buy**
   - Create a trigger to decrease the quantity of an item after adding a new order.
   
6. **Email validation to sent**
   - Create a trigger to reset the attribute `valid_email` only when the email has been changed.
   
7. **Add bonus**
   - Create a stored procedure `AddBonus` to add a new correction for a student.
   
8. **Average score**
   - Create a stored procedure `ComputeAverageScoreForUser` to compute and store the average score for a student.
   
9. **Optimize simple search**
   - Create an index `idx_name_first` on the table `names` for the first letter of name.
   
10. **Optimize search and score**
    - Create an index `idx_name_first_score` on the table `names` for the first letter of name and the score.
    
11. **No table for a meeting**
    - Create a view `need_meeting` to list all students that have a score under 80 and no last meeting or more than 1 month.

## Usage

To use the scripts, follow these steps:
- Clone the repository to your local machine.
- Run the SQL scripts using MySQL 5.7 with Ubuntu 18.04 LTS.
- Ensure the scripts are executed in the specified order to meet dependencies.

## Resources

- MySQL cheatsheet
- MySQL Performance: How To Leverage MySQL Database Indexing
- Stored Procedure
- Triggers
- Views
- Functions and Operators
- Trigger Syntax and Examples
- CREATE TABLE Statement
- CREATE PROCEDURE and CREATE FUNCTION Statements
- CREATE INDEX Statement
- CREATE VIEW Statement

## Credits

This project is part of the curriculum at [Holberton School](https://www.holbertonschool.com/).

