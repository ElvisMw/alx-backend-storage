-- Create table users with specific attributes

-- If the table already exists, your script should not fail
CREATE TABLE IF NOT EXISTS users (
     -- id, integer, never null, auto increment and primary key
    id INT AUTO_INCREMENT PRIMARY KEY,
     -- email, string (255 characters), never null and unique
    email VARCHAR(255) UNIQUE NOT NULL,
     -- name, string (255 characters)
    name VARCHAR(255)
);
