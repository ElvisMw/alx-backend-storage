-- Select users with emails containing "gmail.com" but not "yahoo.com"
SELECT *
FROM users
-- Emails containing "gmail.com"
WHERE email LIKE '%gmail.com' 
-- Emails not containing "yahoo.com"
AND email NOT LIKE '%yahoo.com%';
