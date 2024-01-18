import streamlit as st
import os
import toml

# Specify the full path to the secrets.toml file
script_directory = os.path.dirname(os.path.abspath(__file__))
secrets_path = os.path.join(script_directory, ".streamlit/secrets.toml")

# Load database configuration from secrets.toml
with open(secrets_path, "r") as f:
    secrets_config = toml.load(f)

# Extract the MySQL configuration
mysql_config = secrets_config["mysql"]

# Establish the connection
conn = st.experimental_connection('mysql', config=mysql_config)

# Query the database
df = conn.query('SELECT * from mytable;', ttl=600)

# Display the results
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")



