-- Question: which customer segments paid the Q3 2026 revenue?
-- Grain of result: one row per segment. Grain of input: one row per paid invoice.
-- Segment is the account's current classification. Historical segmentation needs dated membership.
-- Same revenue definition and exclusions as monthly_revenue.sql, so the segment total must
-- equal the July-September total there. That equality is the reconciliation check.
SELECT a.segment,
       SUM(i.amount_cents) / 100.0  AS revenue_usd,
       COUNT(DISTINCT i.account_id) AS paying_accounts
FROM invoices AS i
JOIN accounts AS a ON a.account_id = i.account_id
WHERE i.status = 'paid'
  AND a.is_test = 0
  AND i.invoice_date >= '2026-07-01' AND i.invoice_date < '2026-10-01'   -- half-open date range
GROUP BY a.segment
ORDER BY revenue_usd DESC;
