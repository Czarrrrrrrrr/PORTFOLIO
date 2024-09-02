from pathlib import Path 
import streamlit as st
from PIL import Image

# Setting up paths
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic_path = current_dir / "assets" / "profile-pic.png"

NAME = "Czar Philip Montallana Buot"
DESCRIPTION = """
Avid IT student eager to apply skills in software development, network management, and cybersecurity. Passionate about learning, contributing to innovative projects, and seeking a challenge in the field of Information Technology.

"""
EMAIL = "czarphilip00@gmail.com"
SOCIAL_MEDIA = {
    ">> Facebook <<": "https://www.facebook.com/philippoy00",
    ">> Instagram <<": "https://www.instagram.com/whosczarrr",
}
BIOGRAPHY = """
My name is Czar Philip Montallana Buot, and I was born on June 10, 2002, in Cebu Velez Hospital in Cebu City. I'm 22 years old and currently pursuing a Bachelor of Science in Information Technology at Cebu Institute of Technology - University. I started my junior high at the University of San Jose-Recoletos before transferring for senior high, continuing into college. I aspire to become a dedicated and enthusiastic computer programmer. One of my childhood achievements includes earning the 'Best in Spelling' award during grade school. My all-time favorite food is 'Pares,' which always makes me hungrier. In my free time, I enjoy going to the gym for at least an hour or so, as I see myself achieving a great physique in 2-3 years with discipline and hard work.
"""

# Portfolio data
PORTFOLIO = [
    {
        "title": "Capstone Project",
        "description": "An instructional material printing request system designed for Wildcats Innovation Labs to streamline the printing process for textbooks, laboratory manuals, and office forms.",
        "image": str(current_dir / "assets" / "project1.png"),  # Convert Path to string
    }
]

# Load CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Additional CSS to justify text and set font
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    .justified-text {
        text-align: justify;
        font-family: 'Roboto', sans-serif;
    }

    body {
        font-family: 'Roboto', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Display profile picture and bio
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    if profile_pic_path.exists():
        profile_pic = Image.open(profile_pic_path)
        st.image(profile_pic, width=230)
    else:
        st.write("Image file does not exist.")

with col2:
    st.title(NAME)
    st.markdown(f"<div class='justified-text'>{DESCRIPTION}</div>", unsafe_allow_html=True)
    st.write("📧", EMAIL)  # Email displayed after description

# Display Social Media Links
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Display Biography
st.write('\n')
st.subheader("Biography")
st.markdown(f"<div class='justified-text'>{BIOGRAPHY}</div>", unsafe_allow_html=True)

# Display Personal Skills
st.write('\n')
st.subheader("Personal Skills")
st.write(
    """
- 📂 MS Office    
- 👩‍💻 Programming: Python, Java, C/C++
- 🌐 Web Development: HTML/CSS
- 📊 Data Visualization: PowerBi, MS Excel
- 🗄️ Databases: MySQL
- 🗣️ Languages: English, Filipino, Cebuano
"""
)

# Display Portfolio
st.write('\n')
st.subheader("Portfolio")

for project in PORTFOLIO:
    col1, col2 = st.columns([1, 2])
    with col1:
        image_path = Path(project["image"])
        if image_path.exists():
            st.image(image_path, use_column_width=True)
        else:
            st.write("Image file does not exist.")
    with col2:
        st.markdown(f"**{project['title']}**")
        st.markdown(f"<div class='justified-text'>{project['description']}</div>", unsafe_allow_html=True)
