.read data.sql

-- QUESTIONS --



-------------------------------------------------------------------------
------------------------ Give Interest- ---------------------------------
-------------------------------------------------------------------------

update accounts set amount = 1.02*amount;

create table give_interest_result as select * from accounts; -- just for tests

-------------------------------------------------------------------------
------------------------ Split Accounts ---------------------------------
-------------------------------------------------------------------------

create table checkaccounts as select name || "'s Checking account" as name,amount/2 as amount from accounts;
update accounts set name = name || "'s Savings account", amount = amount/2;
insert into accounts select name, amount from checkaccounts;


create table split_account_results as select * from accounts; -- just for tests

-------------------------------------------------------------------------
-------------------------------- Whoops ---------------------------------
-------------------------------------------------------------------------

drop table accounts ;


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price
  from products 
  group by category;

CREATE TABLE lowest_prices AS
  SELECT store,item,min(price)
  from inventory 
  group by item;


CREATE TABLE shopping_list AS
SELECT t.name, l.store
from (select category, name, MSRP, min(MSRP/rating) from products group by category) as t
left join lowest_prices as l
on t.name = l.item
order by t.name;

CREATE TABLE total_bandwidth AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
