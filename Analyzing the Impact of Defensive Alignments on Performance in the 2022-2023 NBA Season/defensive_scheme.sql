Copy
-- Query to calculate PPP and eFG% by defensive scheme
SELECT 
  game_id,
  defensive_scheme, -- e.g., 'man', 'zone', 'hybrid', 'switch'
  AVG(opponent_points / possessions) AS avg_ppp,
  AVG((opponent_fgm + 0.5 * opponent_3pm) / opponent_fga) AS avg_efg,
  COUNT(*) AS total_possessions
FROM 
  nba_defensive_possessions
WHERE 
  season = '2022-2023'
  AND defensive_scheme IS NOT NULL
GROUP BY 
  game_id, defensive_scheme;
