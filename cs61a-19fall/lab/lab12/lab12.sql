.read fa19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor
  from students;

CREATE TABLE smallest_int AS
  SELECT time, smallest
  from students 
  where smallest > 2
  order by smallest
  limit 20;

CREATE TABLE matchmaker AS
  SELECT s1.pet, s2.song, s1.color, s2.color
  from students as s1 join students as s2 
  on s1.pet = s2.pet and s1.song = s2.song
  where s1.time < s2.time;

