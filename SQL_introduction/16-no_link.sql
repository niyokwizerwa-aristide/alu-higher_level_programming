-- Lists all records of second_table that have a name, ordered by score (top first)
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
