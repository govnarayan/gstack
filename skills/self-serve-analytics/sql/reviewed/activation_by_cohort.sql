-- Question: what share of new accounts activate within 14 days, by signup month?
-- Activated = within 14 days of account creation, some user created a project AND some user invited a teammate.
-- Grain of result: one row per signup month. Denominator: every eligible account, including accounts with no events.
-- Eligibility: not a test account, and the 14-day window of the cohort's LAST possible member (month end) closed
-- before the event data was loaded (maturity rule applied to the whole cohort, not member by member).
-- Dates: stored timestamps use 'T'; SQLite datetime() returns a space. Wrap BOTH sides in datetime() before comparing.
WITH cohort AS (
  SELECT account_id, substr(created_at, 1, 7) AS cohort_month, created_at
  FROM accounts
  WHERE is_test = 0
    AND datetime(created_at, 'start of month', '+1 month', '+14 days')
        <= (SELECT datetime(loaded_through) FROM load_log WHERE table_name = 'events')
),
early AS (
  SELECT c.account_id,
         MAX(e.event_type = 'create_project')  AS made_project,
         MAX(e.event_type = 'invite_teammate') AS invited
  FROM cohort AS c
  JOIN users  AS u ON u.account_id = c.account_id
  JOIN events AS e ON e.user_id = u.user_id
  WHERE datetime(e.occurred_at) >= datetime(c.created_at)
    AND datetime(e.occurred_at) < datetime(c.created_at, '+14 days')
  GROUP BY c.account_id                   -- back to one row per account before counting
)
SELECT c.cohort_month,
       COUNT(*)                                               AS accounts,
       SUM(COALESCE(early.made_project AND early.invited, 0)) AS activated,
       ROUND(1.0 * SUM(COALESCE(early.made_project AND early.invited, 0)) / COUNT(*), 4) AS activation_rate
FROM cohort AS c
LEFT JOIN early ON early.account_id = c.account_id   -- LEFT keeps accounts that never acted
GROUP BY c.cohort_month
ORDER BY c.cohort_month;
