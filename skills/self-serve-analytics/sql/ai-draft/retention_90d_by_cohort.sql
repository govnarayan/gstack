-- AI first draft. Request given: "90-day retention by first-subscription month"
-- It counts an account as retained when it is still subscribed TODAY, and it keeps cohorts whose
-- 90-day window has not closed.
WITH firsts AS (
  SELECT s.account_id, MIN(s.started_at) AS first_start
  FROM subscriptions AS s
  JOIN accounts AS a ON a.account_id = s.account_id
  WHERE a.is_test = 0
  GROUP BY s.account_id
),
flags AS (
  SELECT f.account_id, substr(f.first_start, 1, 7) AS cohort_month,
         EXISTS (SELECT 1 FROM subscriptions AS s
                 WHERE s.account_id = f.account_id AND s.ended_at IS NULL) AS retained
  FROM firsts AS f
)
SELECT cohort_month,
       COUNT(*)                                 AS accounts,
       SUM(retained)                            AS retained_90d,
       ROUND(1.0 * SUM(retained) / COUNT(*), 4) AS retention_90d
FROM flags
GROUP BY cohort_month
ORDER BY cohort_month;
