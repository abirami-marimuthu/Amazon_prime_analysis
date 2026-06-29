-- View first 10 rows
SELECT *
FROM amazon_prime
LIMIT 10;

-- Total Shows
SELECT COUNT(*) AS total_shows
FROM amazon_prime;

-- Average IMDb Rating
SELECT ROUND(AVG("IMDb_Rating"),2) AS avg_rating
FROM amazon_prime;

-- Highest IMDb Rating
SELECT MAX("IMDb_Rating") AS highest_rating
FROM amazon_prime;

-- Top 10 Genres
SELECT Genre,
       COUNT(*) AS total
FROM amazon_prime
GROUP BY Genre
ORDER BY total DESC
LIMIT 10;

-- Top Languages
SELECT Language,
       COUNT(*) AS total
FROM amazon_prime
GROUP BY Language
ORDER BY total DESC;

-- Shows released over years
SELECT Release_Year,
       COUNT(*) AS total_shows
FROM amazon_prime
GROUP BY Release_Year
ORDER BY Release_Year;

-- Top Rated Shows
SELECT Show_Name,
       "IMDb_Rating"
FROM amazon_prime
ORDER BY "IMDb_Rating" DESC
LIMIT 10;