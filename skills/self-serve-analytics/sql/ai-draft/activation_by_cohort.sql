-- AI first draft. Request given: "activation rate by signup month; activated means created a project
-- and invited a teammate in the first 14 days"
SELECT substr(a.created_at, 1, 7) AS cohort_month,
       COUNT(DISTINCT a.account_id) AS accounts,
       COUNT(DISTINCT CASE WHEN e.event_type IN ('create_project', 'invite_teammate')
                            AND e.occurred_at < datetime(a.created_at, '+14 days')
                           THEN a.account_id END) AS activated,
       COUNT(DISTINCT CASE WHEN e.event_type IN ('create_project', 'invite_teammate')
                            AND e.occurred_at < datetime(a.created_at, '+14 days')
                           THEN a.account_id END) / COUNT(DISTINCT a.account_id) AS activation_rate
FROM accounts AS a
JOIN users  AS u ON u.account_id = a.account_id
JOIN events AS e ON e.user_id = u.user_id
GROUP BY 1
ORDER BY 1;
