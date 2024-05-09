-- Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    -- Unique identifier for each user
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    -- Email address of the user, must be unique
    email VARCHAR(255) NOT NULL UNIQUE,
    -- Name of the user
    name VARCHAR(255),
    -- Country of the user, limited to specific values
    country ENUM('US', 'CO', 'TN') NOT NULL
);
