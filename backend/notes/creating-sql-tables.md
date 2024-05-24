# Creating SQL Tables

```SQL
CREATE TABLE table_name (
    column1_name TYPE CONSTRAINTS,
    column2_name TYPE(args) CONSTRAINTS,
    ...
);
```

## Example

```SQL
CREATE TABLE table_name (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    ...
);
```
