import streamlit as st
import duckdb

# Function to retrieve data from the DuckDB database
def retrieve_data():
    connection = duckdb.connect(database='openai_data.duckdb')
    cursor = connection.cursor()
    cursor.execute("SELECT value FROM openai_data.ai_movies.movies__value")
    result = cursor.fetchall()
    connection.close()
    return result

# Load the data using Streamlit's caching command
@st.cache_data
def load_data():
    return retrieve_data()

def main():
    st.title("Top AI(Artifical Intelligence) Themed Movies")

    # Load the data
    data = load_data()

    # Add the first element from the list, which corresponds to the movie names
    movies = []
    for i in range(0, len(data), 2):
        movies.append(data[i][0])


    # Display the movies as a list
    for index, movie in enumerate(movies, start=1):
        st.write(f"{movie}")

if __name__ == "__main__":
    main()
