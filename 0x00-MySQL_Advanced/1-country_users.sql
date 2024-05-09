-- Select all users whose email addresses contain "gmail.com"
SELECT *
FROM users AS u1
WHERE email LIKE '%gmail.com'
-- Check if there are no corresponding users with email addresses containing "yahoo.com"
AND NOT EXISTS (
    SELECT *
    FROM users AS u2
    WHERE u1.id = u2.id
    AND u2.email LIKE '%yahoo.com%'
);
