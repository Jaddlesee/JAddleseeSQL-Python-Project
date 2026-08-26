/*SELECT
    t.tier_name AS MembershipTier,
    COUNT(m.member_id) AS MemberCount
FROM membTiers t
LEFT JOIN members m
    ON m.tier_id = t.tier_id
GROUP BY t.tier_id, t.tier_name */
-- Counts how many members in each tier

/*SELECT
    t.tier_name,
    COUNT(CASE WHEN m.membership_status = 'Active' THEN m.member_id END) AS active_subscriptions,
    ROUND(100 * SUM(CASE WHEN m.membership_status = 'Active' THEN 1 ELSE 0 END) / COUNT(m.member_id), 2) AS active_percentage,
    t.monthly_price,
    COUNT(CASE WHEN m.membership_status = 'Active' THEN m.member_id END) * t.monthly_price AS expected_monthly_income
FROM membTiers AS t
LEFT JOIN members AS m
    ON m.tier_id = t.tier_id
GROUP BY
    t.tier_id,
    t.tier_name,
    t.monthly_price
ORDER BY expected_monthly_income DESC; */
-- Filters to active subscribers and the expected monthly income from each tier, also works out the percentage of each membership tier members that are actively subscribed

/*SELECT
    m.member_id,
    m.first_name,
    m.last_name,
    m.membership_status,
    t.tier_name,
    m.member_since
FROM members AS m
JOIN membTiers AS t
    ON m.tier_id = t.tier_id
ORDER BY m.member_since ASC
LIMIT 10; */
-- Only shows the 10 most oldest members and the status of their memberships