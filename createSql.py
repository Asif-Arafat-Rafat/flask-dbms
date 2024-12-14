import re
from col_data import col
from helper import printMe,garbagefilter
import random
table_info={}

def spliter(col):
    br=re.findall(r"(\(.*?\))",col,re.DOTALL|re.IGNORECASE)
    brc={}
    for b in br:
        var= f"___BRprotEction_{random.randint(100000,999999)}"
        brc[var]=b
        col=col.replace(b,var)
    # print(brc)
    ecol= re.findall(r"(.*?)(?:,|$)",col,re.DOTALL|re.IGNORECASE)
    for i ,e in enumerate(ecol):
        ecol[i]=ecol[i].strip(" ")
        for k,v in brc.items():
            ecol[i]=ecol[i].replace(k,v)
    return ecol
        


def extract_table_data(content,checked):
    if checked is True:
        chk=f"./tmp/{content}CreateTab.tql"
        with open(chk,'r') as c:
            content=c.read()
    info={}
    fnd= re.findall(r"create table\s*(IF NOT EXISTS)?\s*(`[^`]*`|\S+)\s\((.*?)\s*;",content,re.IGNORECASE|re.DOTALL)
    for i in fnd:
        n=re.findall(r".*\)",i[2],re.DOTALL|re.IGNORECASE)
        a=n[0].replace('\n',"").strip().replace("  "," ")
        a=a[:-1] if a[-1]==")" else a 
        a=spliter(a)
        info[i[1]]=a
    return info
    
# extract_table_data("""CREATE TABLE if not exists projects (
#     project_id INT PRIMARY KEY,
#     project_name VARCHAR2(200),
#     course_id INT,
#     submission_status NUMBER(1) DEFAULT 0, 
#     start_date DATE,
#     end_date DATE,
#     FOREIGN KEY (course_id) REFERENCES projectcourses(course_id) 
#     ON DELETE CASCADE
# );
# """,False)
# extract_table_data("""CREATE TABLE `admin profiles` (
#     `admin_id` int(11) NOT NULL,
#     `username` text NOT NULL,
#     `password` text NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
# """,False)

# extract_table_data("""-- Basic table with a simple primary key
# CREATE TABLE basic_table (
#     id INT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL
# );

# -- Table with ENUM type and DEFAULT value
# CREATE TABLE enum_example (
#     id INT PRIMARY KEY,
#     status ENUM('active', 'inactive', 'pending') DEFAULT 'active'
# );

# -- Table with multiple constraints (UNIQUE, CHECK)
# CREATE TABLE constraints_table (
#     id INT PRIMARY KEY,
#     name VARCHAR(50) UNIQUE,
#     age INT CHECK (age >= 18)
# );

# -- Table with composite primary key and unique constraints
# CREATE TABLE composite_key_table (
#     user_id INT,
#     project_id INT,
#     role VARCHAR(50),
#     PRIMARY KEY (user_id, project_id),
#     UNIQUE (user_id, role)
# );

# -- Table with column-level constraints and default values
# CREATE TABLE column_constraints_table (
#     id INT PRIMARY KEY,
#     email VARCHAR(100) NOT NULL DEFAULT 'example@example.com',
#     active BOOLEAN DEFAULT TRUE
# );

# -- Table with ON DELETE and ON UPDATE actions for foreign keys
# CREATE TABLE foreign_key_actions (
#     order_id INT PRIMARY KEY,
#     customer_id INT,
#     FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
#     ON DELETE SET NULL
#     ON UPDATE CASCADE
# );

# -- Table with GENERATED columns
# CREATE TABLE generated_column_example (
#     base_value INT,
#     tax_rate DECIMAL(5, 2),
#     total_value AS (base_value * tax_rate) STORED
# );

# -- Table using a different storage engine (MySQL specific)
# CREATE TABLE custom_engine_table (
#     id INT PRIMARY KEY,
#     data TEXT
# ) ENGINE=MyISAM;

# -- Table with a spatial index (MySQL specific)
# CREATE TABLE spatial_table (
#     id INT PRIMARY KEY,
#     location POINT NOT NULL,
#     SPATIAL INDEX (location)
# );

# -- Table with partitioning (MySQL specific syntax)
# CREATE TABLE partitioned_table (
#     id INT NOT NULL,
#     name VARCHAR(100),
#     created_at DATE NOT NULL,
#     PRIMARY KEY (id, created_at)
# )
# PARTITION BY RANGE (YEAR(created_at)) (
#     PARTITION p0 VALUES LESS THAN (2000),
#     PARTITION p1 VALUES LESS THAN (2010),
#     PARTITION p2 VALUES LESS THAN MAXVALUE
# );

# -- Table with inheritance (PostgreSQL specific syntax)
# CREATE TABLE parent_table (
#     id SERIAL PRIMARY KEY,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# CREATE TABLE child_table (
#     additional_info TEXT
# ) INHERITS (parent_table);

# -- Table with array data type (PostgreSQL specific)
# CREATE TABLE array_table (
#     id SERIAL PRIMARY KEY,
#     tags TEXT[]
# );

# -- Table with JSON and JSONB data types (PostgreSQL specific)
# CREATE TABLE json_example (
#     id SERIAL PRIMARY KEY,
#     data JSON,
#     metadata JSONB
# );

# -- Temporary table
# CREATE TEMPORARY TABLE temp_table (
#     session_id INT PRIMARY KEY,
#     data TEXT
# );

# -- Table with FOREIGN KEY referencing a composite primary key
# CREATE TABLE referenced_table (
#     id INT,
#     type VARCHAR(20),
#     description TEXT,
#     PRIMARY KEY (id, type)
# );

# CREATE TABLE referencing_table (
#     record_id INT,
#     record_type VARCHAR(20),
#     data TEXT,
#     FOREIGN KEY (record_id, record_type) REFERENCES referenced_table(id, type)
# );

# -- Table with TEXT and BLOB data types
# CREATE TABLE text_blob_table (
#     id INT PRIMARY KEY,
#     description TEXT,
#     file_data BLOB
# );

# -- Table with TIME and INTERVAL types (PostgreSQL specific)
# CREATE TABLE time_interval_table (
#     id SERIAL PRIMARY KEY,
#     start_time TIME,
#     duration INTERVAL
# );

# -- Table with various number data types
# CREATE TABLE number_types (
#     small_number SMALLINT,
#     medium_number INT,
#     large_number BIGINT,
#     precise_number DECIMAL(15, 5),
#     floating_number FLOAT
# );

# -- Table with a trigger-based primary key (example for Oracle)
# CREATE TABLE trigger_example (
#     id NUMBER PRIMARY KEY,
#     description VARCHAR2(100)
# );

# -- Indexes defined directly in the CREATE TABLE
# CREATE TABLE indexed_table (
#     id INT PRIMARY KEY,
#     name VARCHAR(100),
#     INDEX (name)
# );
# """,False)