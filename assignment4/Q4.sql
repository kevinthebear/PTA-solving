CREATE TABLE temp AS
SELECT tradingitemid, pricingdate, adjustedprice, sector
FROM temp_sector
ORDER BY sector, pricingdate, tradingitemid

CREATE TABLE temp_result AS
SELECT DISTINCT tp.pricingdate,
                tp.tradingitemid,
                tp.adjustedprice AS adj_priceclose,
                tp.sector,
                rs.adj_priceclose AS sector_adjustedprice
FROM temp AS tp
LEFT JOIN resultq3 AS rs ON tp.sector = rs.sector AND tp.pricingdate = rs.pricingdate
ORDER BY tp.sector, tp.pricingdate

CREATE TABLE resultq4 AS
SELECT tradingitemid, pricingdate, adj_priceclose, (CASE WHEN adj_priceclose < sector_adjustedprice THEN 'Below sector average' ELSE 'Above sector average' END) AS status
FROM temp_result
ORDER BY tradingitemid, pricingdate
