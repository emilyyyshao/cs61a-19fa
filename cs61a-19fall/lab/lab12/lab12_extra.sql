.read lab12.sql

CREATE TABLE smallest_int_having AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

CREATE TABLE fa19favpets AS
  SELECT pet, count(*) as counts
  from students
  group by pet
  order by counts desc
  limit 10;


CREATE TABLE fa19dog AS
  SELECT pet, count(*) as counts
  from students
  group by pet
  order by counts desc
  limit 1;


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(*)
  from students
  where seven = '7'
  group by instructor;
