-- Selects the origin country and counts the number of fans for each country
SELECT origin, COUNT(*) AS nb_fans
-- Specifies the table to select data from
FROM metal_bands
-- Groups the results by origin country
GROUP BY origin
-- Orders the results by the number of fans in descending order
ORDER BY nb_fans DESC;
