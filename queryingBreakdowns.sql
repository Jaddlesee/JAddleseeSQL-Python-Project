SELECT
    t.tier_name AS MembershipTier,
    COUNT(m.member_id) AS MemberCount
FROM membTiers t
LEFT JOIN members m
    ON m.tier_id = t.tier_id
GROUP BY t.tier_id, t.tier_name
