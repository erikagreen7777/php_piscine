SELECT floor_number AS 'floor', sum(nb_seats) as 'nb_seats'
  FROM cinema
  GROUP BY floor_number
  ORDER BY nb_seats DESC;

