import streamlit as st

# Specify the path to the secrets.toml file
secrets_path = "/workspaces/phpmyadminstreamlit/.streamlit/secrets.toml"

# Load database configuration from secrets.toml
mysql_config = st.secrets["mysql"]

# Establish the connection
conn = st.experimental_connection('mysql', config=mysql_config)

# Query the database
df = conn.query('SELECT * from mytable;', ttl=600)

# Display the results
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
