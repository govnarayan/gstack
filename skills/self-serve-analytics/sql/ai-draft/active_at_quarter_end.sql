-- AI first draft. Request given: "active paying accounts and MRR on 2026-09-30"
SELECT COUNT(DISTINCT s.account_id) AS active_accounts,
       SUM(s.mrr_cents) / 100.0     AS mrr_usd
FROM subscriptions AS s
JOIN accounts AS a ON a.account_id = s.account_id
WHERE a.is_test = 0
  AND s.started_at <= '2026-09-30'
  AND s.ended_at > '2026-09-30';
