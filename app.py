import streamlit as st

# Title and UI Settings
st.set_page_config(page_title="LLM Education Platform", page_icon="🎓", layout="wide")

# Pages Navigation
def main():
    menu = ["Home", "About Us", "Contact Us", "Sign In"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        home_page()
    elif choice == "About Us":
        about_us_page()
    elif choice == "Contact Us":
        contact_us_page()
    elif choice == "Sign In":
        sign_in_page()

# Home Page
def home_page():
    st.markdown("<h1 style='text-align: center; color: darkblue;'>Welcome to LLM Education Platform</h1>", unsafe_allow_html=True)
    st.markdown("### Select Your Class and Course")

    # Class Selection
    class_selection = st.selectbox("Select Class", ["Select", "Class 1", "Class 2", "Class 3"])

    # Course Selection
    if class_selection != "Select":
        course_selection = st.selectbox("Select Course", ["Select", "Mathematics", "Science", "History"])
        if course_selection != "Select":
            st.markdown(f"### {course_selection} Resources")
            st.write("**Videos**")
            st.video("https://example.com/video.mp4")  # Replace with actual URLs
            st.write("**Audio**")
            st.audio("https://example.com/audio.mp3")  # Replace with actual URLs
            st.write("**PDF Files**")
            st.download_button(label="Download PDF", data=b"PDF data", file_name="sample.pdf", mime="application/pdf")  # Replace with actual PDF data

# Sign In Page
def sign_in_page():
    st.markdown("<h2 style='color: darkgreen;'>Sign In with Mobile Number</h2>", unsafe_allow_html=True)
    mobile_number = st.text_input("Enter Mobile Number", max_chars=11, placeholder="03001234567")
    if st.button("Sign In"):
        if mobile_number:
            st.success("Signed in successfully")
            home_page()
        else:
            st.error("Please enter a valid mobile number")

# About Us Page
def about_us_page():
    st.markdown("<h2 style='color: darkorange;'>About Us</h2>", unsafe_allow_html=True)
    st.write("Email: email@gmail.com")
    st.write("We provide educational resources for different classes and courses.")

# Contact Us Page
def contact_us_page():
    st.markdown("<h2 style='color: darkred;'>Contact Us</h2>", unsafe_allow_html=True)
    st.write("Phone: 03003976568")
    st.write("Email: email@gmail.com")

# Run the main function
if __name__ == "__main__":
    main()
