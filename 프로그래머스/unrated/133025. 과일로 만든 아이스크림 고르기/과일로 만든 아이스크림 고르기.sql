-- 코드를 입력하세요
SELECT L.FLAVOR
FROM FIRST_HALF L
INNER JOIN ICECREAM_INFO R
    ON L.FLAVOR = R.FLAVOR
WHERE TOTAL_ORDER > 3000 AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC;