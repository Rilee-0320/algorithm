-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, GENDER, COUNT(DISTINCT R.USER_ID) AS USERS
FROM USER_INFO L
RIGHT JOIN ONLINE_SALE R USING (USER_ID)
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER