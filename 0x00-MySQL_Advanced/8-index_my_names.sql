-- 0x00-MySQL_Advanced\8-index_my_names.sql
-- a SQL script that creates an index idx_name_first on
-- the table names and the first letter of name
CREATE INDEX idx_name_first
 ON names(name(1));