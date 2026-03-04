-- Selects score and the number of occurrences from second_table grouped by score and ordered by number descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;