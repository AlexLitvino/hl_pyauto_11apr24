CREATE TABLE  data (
	data_id INTEGER PRIMARY KEY,
   	data_value TEXT NOT NULL,
   	data_size INTEGER
);
INSERT INTO data (data_value, data_size)
VALUES
   ('line1', 5),
   ('1', 1),
   ('Loooooooooooooooooooooooooond', 999);
