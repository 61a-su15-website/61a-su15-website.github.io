-- Cities
create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,             71,               "Cambridge"        union
  select 45,             93,               "Minneapolis";

-- Parents
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

-- Children of Abraham
select child from parents where parent = "abraham";

-- Fillmores
select parent from parents where parent > child;

----------
-- Dogs --
----------

-- Parents
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

-- Fur
create table dogs as
  select "abraham" as name, "long" as fur union
  select "barack"         , "short"       union
  select "clinton"        , "long"        union
  select "delano"         , "long"        union
  select "eisenhower"     , "short"       union
  select "fillmore"       , "curly"       union
  select "grover"         , "short"       union
  select "herbert"        , "curly";

-- Parents of curly dogs
select parent from parents, dogs where child = name and fur = "curly";

-- Siblings
select a.child as first, b.child as second
  from parents as a, parents as b
  where a.parent = b.parent and a.child < b.child;

-- Grandparents
create table grandparents as
  select a.parent as grandog, b.child as granpup
    from parents as a, parents as b
    where b.parent = a.child;

-- Grandogs with the same fur as their granpups
select grandog, granpup, c.fur from grandparents, dogs as c, dogs as d
  where grandog = c.name  and
        granpup = d.name and
        c.fur = d.fur;

------------
-- Cities --
------------

create table cities as
  select 38 as latitude, 122 as longitude, "Berkeley" as name union
  select 42,              71,              "Cambridge"        union
  select 45,              93,              "Minneapolis"      union
  select 33,             117,              "San Diego"        union
  select 26,              80,              "Miami"            union
  select 90,               0,              "North Pole";

create table cold as
  select name from cities where latitude > 43 union
  select "Chicago";

select name, "is cold!" from cold;

create table distances as
  select a.name as first, b.name as second,
         60*(a.latitude-b.latitude) as distance
         from cities as a, cities as b
         where a.name != b.name
         order by a.longitude;

select second from distances where first="Minneapolis" order by -distance;

-------------
-- Animals --
-------------

create table animals as
  select "dog" as kind, 4 as legs, 20 as weight union
  select "cat"        , 4        , 10           union
  select "ferret"     , 4        , 10           union
  select "parrot"     , 2        , 6            union
  select "penguin"    , 2        , 10           union
  select "t-rex"      , 2        , 12000;

select max(legs) from animals;

select sum(weight) from animals;

select max(legs - weight) + 5 from animals;

select min(legs), max(weight) from animals where kind <> "t-rex";

select max(legs) + min(weight) from animals;

select count(legs) from animals;

select count(*) from animals;

select count(distinct legs) from animals;

select kind, max(weight) from animals;

select legs, max(weight) from animals group by legs;

select weight/legs, count(*) from animals group by weight/legs;

select weight/legs, count(*) from animals group by weight/legs having count(*)>1;

select max(kind), legs, weight from animals group by legs, weight having max(weight) < 100;

