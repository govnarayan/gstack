-- Question: how many paying accounts, and how much monthly recurring revenue (MRR), were active on 2026-09-30?
-- Active on date D = started on or before D and either still open (ended_at IS NULL) or ended after D.
-- Grain: a plan change closes one subscription row and opens another on the same date, so at most one row
-- per account is active on D. COUNT(DISTINCT account_id) still guards against overlapping rows.
SELECT COUNT(DISTINCT s.account_id) AS active_accounts,
       SUM(s.mrr_cents) / 100.0     AS mrr_usd
FROM subscriptions AS s
JOIN accounts AS a ON a.account_id = s.account_id
WHERE a.is_test = 0
  AND s.started_at <= '2026-09-30'
  AND (s.ended_at IS NULL OR s.ended_at > '2026-09-30');
