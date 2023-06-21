DROP TABLE IF EXISTS locations;

CREATE TABLE IF NOT EXISTS locations (
  id SERIAL PRIMARY KEY,
  city VARCHAR (255),
  state VARCHAR (255),
  country VARCHAR (255)
);

INSERT INTO locations (city, state, country) VALUES
('New York','New York','USA'),
('Reykjavík','N/A','Iceland'),
('Camden','New Jersey','USA'),
('Philadelphia','Pennsylvania','USA');
;
