-- AI first draft. Request given: "Q3 revenue by segment, only for accounts that still have active users"
SELECT a.segment,
       SUM(i.amount_cents) / 100.0  AS revenue_usd,
       COUNT(DISTINCT i.account_id) AS paying_accounts
FROM invoices AS i
JOIN accounts AS a ON a.account_id = i.account_id
JOIN users    AS u ON u.account_id = a.account_id AND u.deactivated_at IS NULL
WHERE i.status = 'paid'
  AND a.is_test = 0
  AND i.invoice_date BETWEEN '2026-07-01' AND '2026-09-30'
GROUP BY a.segment
ORDER BY revenue_usd DESC;
