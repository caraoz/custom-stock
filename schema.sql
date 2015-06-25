CREATE TABLE assets(
asset_id INTEGER not null primary key,
ticker TEXT,
tag TEXT);

CREATE TABLE prices(
price_id INTEGER not null primary key,
asset_id integer not null,
gregorian_day INTEGER,
date_string DATE,
year INTEGER,
month INTEGER,
day INTEGER,
open REAL,
close REAL,
high REAL,
low REAL,
volume INTEGER,
FOREIGN KEY (asset_id) REFERENCES assets(asset_id))