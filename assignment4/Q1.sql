SELECT COUNT(DISTINCT tradingitemid)
    FROM info
    WHERE webpage not like 'www.%' OR webpage IS NULL
