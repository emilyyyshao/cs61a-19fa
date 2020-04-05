CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name as name, s.size as size
  from dogs as d, sizes as s
  where d.height > s.min and d.height <= s.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  select p.child
  from parents as p, dogs as d
  where p.parent = d.name  
  order by d.height desc;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT p1.child as child1, p2.child as child2
  from parents as p1, parents as p2
  where p1.parent = p2.parent and p1.child < p2.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT s1.child1 || ' and ' || s1.child2 || ' are ' || s2.size || ' siblings'
  from siblings as s1, size_of_dogs as s2, size_of_dogs as s3
  where s1.child1 = s2.name and s1.child2 = s3.name and s2.size = s3.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

  insert into stacks_helper select name, height, height from dogs;
  insert into stacks_helper select s1.dogs ||', '|| d.name , s1.stack_height + d.height, d.height from stacks_helper as s1, dogs as d where s1.last_height < d.height;
  insert into stacks_helper select s2.dogs ||', '|| d.name , s2.stack_height + d.height, d.height from stacks_helper as s2, dogs as d where s2.last_height < d.height;
  insert into stacks_helper select s3.dogs ||', '|| d.name , s3.stack_height + d.height, d.height from stacks_helper as s3, dogs as d where s3.last_height < d.height;

CREATE TABLE stacks AS
  SELECT dogs,stack_height
  from stacks_helper
  where stack_height > 170 
  order by stack_height ;
