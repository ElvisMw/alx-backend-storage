-- This query lists all bands with Glam rock as their main style, ranked by their longevity.
-- The query joins the metal_bands table with the bands table to obtain the band_name, and calculates the lifespan of each band by subtracting the formed year from the split year or the current year if the band is still active.
-- The result is sorted in descending order by lifespan.
SELECT
  band_name,
  -- Calculate the lifespan of each band by subtracting the formed year from the split year or the current year if the band is still active.
  (IFNULL(split, YEAR(CURDATE())) - formed) AS lifespan
FROM
  metal_bands
  -- Join the metal_bands table with the bands table to obtain the band_name.
  JOIN bands USING (band_id)
WHERE
  -- Filter the bands with Glam rock as their main style.
  style LIKE '%Glam rock%'
ORDER BY
  -- Sort the result in descending order by lifespan.
  lifespan DESC;
AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
