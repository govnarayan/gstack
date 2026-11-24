-- Question: how much subscription revenue did customers pay each month?
-- Grain of result: one row per invoice month. Grain of input: one row per invoice.
-- Definition: collected revenue = invoices with status 'paid'. Void and refunded invoices are excluded.
-- Exclusions: internal test accounts (accounts.is_test = 1).
-- Join check: each invoice has exactly one account, so this join cannot multiply invoice rows.
SELECT substr(i.invoice_date, 1, 7)      AS month,
       SUM(i.amount_cents) / 100.0        AS revenue_usd,   -- 100.0, not 100: keep cents
       COUNT(*)                           AS paid_invoices
FROM invoices AS i
JOIN accounts AS a ON a.account_id = i.account_id
WHERE i.status = 'paid'
  AND a.is_test = 0
GROUP BY 1
ORDER BY 1;
