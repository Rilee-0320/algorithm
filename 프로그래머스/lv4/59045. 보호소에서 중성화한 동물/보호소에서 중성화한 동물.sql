-- 코드를 입력하세요
SELECT ANIMAL_ID, L.ANIMAL_TYPE, L.NAME
FROM ANIMAL_INS L
INNER JOIN ANIMAL_OUTS R USING (ANIMAL_ID)
WHERE SEX_UPON_INTAKE LIKE 'Intact%' AND SEX_UPON_OUTCOME REGEXP 'Spayed|Neutered'
ORDER BY ANIMAL_ID; 