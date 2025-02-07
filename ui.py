import streamlit as st
import requests

st.title("Custom Chatbot ")
st.write("Ask about technical courses!")


user_query = st.text_input("Enter your query:")

if st.button("Search"):
    if user_query:
        response = requests.post(
            "http://127.0.0.1:5000/search",
            json={"query": user_query}
        )
        if response.status_code == 200:
            courses = response.json().get("matches", [])
            if courses:
                st.success("Found similar courses:")
                for idx, course in enumerate(courses, 1):
                    st.write(f"**{idx}.** {course}")
            else:
                st.warning("No similar courses found.")
        else:
            st.error("Error fetching response.")
    else:
        st.warning("Please enter a query.")
