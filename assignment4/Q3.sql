CREATE TABLE price_factor AS
SELECT DISTINCT cp.tradingitemid,
                cp.pricingdate,
                cp.priceclose,
                da.fromdate,
                da.todate,
                COALESCE(da.divadjfactor, '1') AS divfactor
FROM close_price AS cp
LEFT JOIN dividend_adjustment AS da ON cp.tradingitemid = da.tradingitemid AND (cp.pricingdate BETWEEN fromdate AND todate)
ORDER BY cp.tradingitemid

CREATE TABLE adjustedprice AS
SELECT tradingitemid, pricingdate, priceclose*divfactor AS adjustedprice
FROM price_factor

CREATE TABLE temp_sector AS
SELECT DISTINCT ap.tradingitemid,
                ap.pricingdate,
                ap.adjustedprice,
                sc.sector,
                sc.startdate,
                sc.enddate
FROM adjustedprice AS ap
LEFT JOIN sector AS sc ON ap.tradingitemid = sc.listingid AND (ap.pricingdate BETWEEN sc.startdate AND sc.enddate)
ORDER BY ap.tradingitemid

CREATE TABLE resultq3 AS
SELECT sector, pricingdate, AVG(adjustedprice) AS adj_priceclose
FROM temp_sector
GROUP BY sector, pricingdate
ORDER BY sector, pricingdate