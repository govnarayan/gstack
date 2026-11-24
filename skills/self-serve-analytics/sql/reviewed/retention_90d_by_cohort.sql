-- Question: of accounts that started paying in each month, what share still paid 90 days later?
-- Cohort = month of the account's FIRST subscription start. Retained = an active subscription on start + 90 days.
-- Maturity: show a cohort only when its LAST possible member (month end) has reached day 90 by the load date.
-- Admitting only the early-month members of a young cohort would bias it toward whoever started first.
WITH firsts AS (
  SELECT s.account_id, MIN(s.started_at) AS first_start
  FROM subscriptions AS s
  JOIN accounts AS a ON a.account_id = s.account_id
  WHERE a.is_test = 0
  GROUP BY s.account_id
),
eligible AS (
  SELECT f.account_id, f.first_start, date(f.first_start, '+90 days') AS check_date
  FROM firsts AS f
  WHERE date(f.first_start, 'start of month', '+1 month', '-1 day', '+90 days')
        <= (SELECT date(loaded_through) FROM load_log WHERE table_name = 'subscriptions')
),
flags AS (
  SELECT e.account_id, substr(e.first_start, 1, 7) AS cohort_month,
         EXISTS (SELECT 1 FROM subscriptions AS s
                 WHERE s.account_id = e.account_id
                   AND s.started_at <= e.check_date
                   AND (s.ended_at IS NULL OR s.ended_at > e.check_date)) AS retained
  FROM eligible AS e
)
SELECT cohort_month,
       COUNT(*)                                 AS accounts,
       SUM(retained)                            AS retained_90d,
       ROUND(1.0 * SUM(retained) / COUNT(*), 4) AS retention_90d
FROM flags
GROUP BY cohort_month
ORDER BY cohort_month;
