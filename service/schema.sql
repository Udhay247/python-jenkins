-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS todo;

CREATE TABLE todo (
  id INTEGER,
  task TEXT NOT NULL
);
