-- a SQL script that ranks country origins of bands,
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER nb_fans DESC;
