-- command line
>mysql -u root -p


>mysql --local-infile=1 -u root -p


>load data local infile '<path c:\\users\\...>'
   -> into table tablename
   -> fields terminated by ','
   -> lines terminated by '\r\n'
   -> ignore 1 lines;
   -> enclosed by '"'

