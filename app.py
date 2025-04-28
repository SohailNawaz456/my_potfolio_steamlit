import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

# --- Page Configuration ---
st.set_page_config(page_title="Sohail's Portfolio", page_icon=":sparkles:", layout="wide")

# --- Load Lottie Animations ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_intro = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_1pxqjqps.json")
lottie_coder = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_w51pcehl.json")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    body, .stApp {
        background-color: #121212;
        color: #f5f5f5;
        font-family: 'Poppins', sans-serif;
    }
    h1, h2, h3 {
        color: #00bfff;
    }
    hr {
        border: 1px solid #333333;
    }
    .typing {
        width: 22ch;
        animation: typing 4s steps(22) infinite alternate, blink 0.7s infinite;
        white-space: nowrap;
        overflow: hidden;
        border-right: 3px solid #00bfff;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin: auto;
    }
    @keyframes typing {
        from { width: 0 }
        to { width: 22ch }
    }
    @keyframes blink {
        50% { border-color: transparent }
    }
    form {
        background-color: #1e1e1e;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
        width: 350px;
        margin: auto;
    }
    input, textarea {
        width: 100%;
        padding: 10px;
        margin-top: 10px;
        margin-bottom: 15px;
        background: #2c2c2c;
        border: 1px solid #555555;
        border-radius: 5px;
        color: white;
    }
    button {
        background-color: #00bfff;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
        font-weight: bold;
    }
    button:hover {
        background-color: #0099cc;
    }
    .footer {
        text-align: center;
        padding: 20px;
        font-size: 14px;
        color: #888;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Intro Animation ---
with st.container():
    if lottie_intro:
        st_lottie(lottie_intro, height=300, key="intro", speed=1.2)
    st.markdown("<div class='typing'>Welcome to My Portfolio</div>", unsafe_allow_html=True)
    st.write("##")

# --- Header Section ---
st.subheader("Hey Guys :wave:")
st.title("My Portfolio Website")
st.write("---")
st.write(
    "I am going to explain briefly how Streamlit can be used to build "
    "interactive and responsive websites to deploy any machine learning model."
)
st.write("[Read More](https://streamlit.io/)")
st.write("---")

# --- Navigation Menu ---
selected = option_menu(
    menu_title=None,
    options=["About", "Projects", "Skills", "Contact"],
    icons=["person", "code-slash", "tools", "chat-left-text-fill"],
    orientation="horizontal",
    styles={
        "container": {"background-color": "#1e1e1e"},
        "icon": {"color": "#00bfff", "font-size": "20px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin": "5px"},
        "nav-link-selected": {"background-color": "#00bfff", "color": "white"},
    }
)

# --- About Section ---
if selected == "About":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("I am Sohail Nawaz")
            st.title("Full Stack Developer")
        with col2:
            if lottie_coder:
                st_lottie(lottie_coder, height=300, key="coder")
            else:
                st.write("Animation could not be loaded.")

    st.write("---")
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Education 🎓")
            st.markdown("""
            - **BIT**
                - Computer Science
                - Grade: xyz
            - **P.A.F School Karachi**
                - Grade: abc
            - **Pakistan Air Force Base Faisal**
                - Xth
                - Grade: def
            """)
        with col4:
            st.subheader("Experience 💼")
            st.markdown("""
            - **Full Stack Developer**
                - Duration: 
                - Karachi
            """)

# --- Projects Section ---
if selected == "Projects":
    with st.container():
        st.subheader("My Projects 🚀")

        # Project 1
        col5, col6 = st.columns((1, 2))
        with col5:
            project1_animation = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_puciaact.json")
            if project1_animation:
                st_lottie(project1_animation, height=250, key="project1")
        with col6:
            st.write("### Project 1: Link Sharing App")
            st.write("A real-time link sharing platform built using Streamlit.")

        # Project 2
        col7, col8 = st.columns((1, 2))
        with col7:
            project2_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jtbfg2nb.json")
            if project2_animation:
                st_lottie(project2_animation, height=250, key="project2")
        with col8:
            st.write("### Project 2: Portfolio Website")
            st.write("A personal portfolio website to showcase my skills and projects.")

        # Project 3
        col9, col10 = st.columns((1, 2))
        with col9:
            project3_animation = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")
            if project3_animation:
                st_lottie(project3_animation, height=250, key="project3")
        with col10:
            st.write("### Project 3: Team Collaboration Tool")
            st.write("A tool to manage team tasks and projects collaboratively.")

# --- Skills Section ---
if selected == "Skills":
    with st.container():
        st.subheader("My Skills 🛠️")
        st.write("##")

        skills = [
            ("HTML", 90),
            ("CSS", 85),
            ("JavaScript", 80),
            ("TypeScript", 75),
            ("Python", 95),
            ("Streamlit", 90),
            ("UV", 70),
            ("Chainlit", 80),
            ("Next.js", 85),
        ]

        for skill, percent in skills:
            st.write(f"**{skill}**")
            st.progress(percent)

# --- Contact Section ---
if selected == "Contact":
    with st.container():
        st.subheader("Get in Touch 📧")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/your-email@example.com" method="POST">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" rows="4" required></textarea>
            <button type="submit">Send Message</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <div class="footer">
        Made with ❤️ by Sohail Nawaz | © 2025
    </div>
""", unsafe_allow_html=True)
