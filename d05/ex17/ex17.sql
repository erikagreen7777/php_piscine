SELECT COUNT(*) AS 'nb_susc', FLOOR(AVG(price)) AS 'avg_susc', MOD(SUM(duration_sub), 42) as 'ft'
  FROM subscription;
