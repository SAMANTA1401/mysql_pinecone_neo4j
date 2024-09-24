-- 1. Similarity Search

SELECT * FROM images
WHERE similarity(vector, [0.2, 0.4, ..., 0.6]) > 0.8
ORDER BY similarity DESC
LIMIT 3;


-- 2. K-Nearest Neighbors (KNN)


SELECT * FROM images
ORDER BY distance(vector, [0.2, 0.4, ..., 0.6]) ASC
LIMIT 5;


-- 3. Range Query

SELECT * FROM images
WHERE similarity(vector, [0.2, 0.4, ..., 0.6]) > 0.7;
