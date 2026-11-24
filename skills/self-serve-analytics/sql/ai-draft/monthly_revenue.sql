-- AI first draft, kept unedited to show what review must catch.
-- Request given: "monthly revenue from the invoices table"
SELECT substr(invoice_date, 1, 7) AS month,
       SUM(amount_cents) / 100     AS revenue_usd,
       COUNT(*)                    AS paid_invoices
FROM invoices
GROUP BY 1
ORDER BY 1;
