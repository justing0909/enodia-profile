import streamlit as st
from PIL import Image
import io
import pandas as pd
from datetime import datetime
import os
import base64
import dotenv
# ===== Page Configuration =====
dotenv.load_dotenv()
st.set_page_config(
    page_title="Professional Profile",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Create a container with minimal top padding
with st.container():
    st.markdown("""
    <style>
    .stApp > header {
        background-color: transparent;
    }
    .stApp > header > div {
        padding-top: 0 !important;
    }
    /* Target the main content area */
    .main .block-container {
        padding-top: 0 !important;
    }
    /* Target the first element */
    .main .block-container > div:first-child {
        margin-top: -6rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ===== Image Processing Functions =====
def get_image_base64(image_path, zoom=2.2):
    if 'linkedin_headshot' in image_path:
        # Open and crop/zoom profile image
        img = Image.open(image_path)
        width, height = img.size
        # Crop to center square
        min_dim = min(width, height)
        left = (width - min_dim) // 2
        top = (height - min_dim) // 2
        right = left + min_dim
        bottom = top + min_dim
        img = img.crop((left, top, right, bottom))
        # Zoom in by cropping further
        zoom_dim = int(min_dim / zoom)
        # Adjust left offset to pan the image (negative moves right, positive moves left)
        left = (min_dim - zoom_dim) // 2 + 80  # Added -30 to pan left
        top = (min_dim - zoom_dim) // 2
        right = left + zoom_dim
        bottom = top + zoom_dim
        img = img.crop((left, top, right, bottom))
        img = img.resize((200, 200))
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode()
    else:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

# ===== Image Processing =====
logo_base64 = get_image_base64("Enodia_PNG_02_Transparent_BG.png")
profile_base64 = get_image_base64("linkedin_headshot-2.jpeg")

# ===== Styling and Layout =====
# Import Google Font
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&display=swap" rel="stylesheet">', unsafe_allow_html=True)

# Base styles
st.markdown("""
<style>
body, .stApp, .main {
    background-color: #c9be9d !important;
    font-family: 'Helvetica Neue', Arial, sans-serif;
}
.main {
    padding: 0 2rem 2rem 2rem;
    max-width: 800px;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)

# Image styles
st.markdown("""
<style>
.centered-image {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 150px;
    filter: drop-shadow(0px 4px 6px rgba(0, 0, 0, 0.1));
}
.profile-img {
    border-radius: 50%;
    width: 280px;
    height: 280px;
    object-fit: cover;
    margin: 0 auto;
    display: block;
    border: 4px solid #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

# Typography
st.markdown("""
<style>
.name {
    text-align: center;
    font-size: 2.8rem;
    font-weight: 600;
    margin: 0.5rem 0 0.1rem 0;
    color: #2c3e50;
    letter-spacing: -0.5px;
    font-family: 'Playfair Display', serif;
}
.title {
    text-align: center;
    font-size: 1.4rem;
    color: #34495e;
    margin-bottom: 2.5rem;
    font-weight: 400;
}
</style>
""", unsafe_allow_html=True)

# Link buttons
st.markdown("""
<style>
.link-button {
    display: block;
    width: 100%;
    padding: 1rem;
    margin: 0.8rem 0;
    text-align: center;
    background-color: #8B7355;
    border-radius: 12px;
    text-decoration: none;
    color: #f5f5f5 !important;
    font-weight: 500;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    border: 1px solid rgba(0, 0, 0, 0.05);
}
.link-button:hover {
    background-color: #9B8365;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    color: #f5f5f5 !important;
}
</style>
""", unsafe_allow_html=True)

# Email form
st.markdown("""
<style>
.stTextInput > div > div > input {
    border-radius: 8px;
    border: 2px solid #8B7355;
    padding: 0.8rem;
    background-color: #c9be9d;
}
.email-label {
    text-align: center;
    font-size: 1.4rem;
    font-weight: 400;
    color: #34495e;
    margin: 0.5rem 0 1rem 0;
}
.stButton > button {
    border-radius: 8px;
    background-color: #8B7355;
    color: #f5f5f5;
    border: none;
    padding: 0.8rem 2rem;
    font-weight: 500;
    transition: all 0.3s ease;
    margin: 0 auto;
    display: block;
}
.stButton > button:hover {
    background-color: #9B8365;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

# Stay Connected section
st.markdown("""
<style>
.stay-connected {
    text-align: center;
    font-size: 2.8rem;
    font-weight: 600;
    margin: 4rem 0 0.1rem 0;
    color: #2c3e50;
    letter-spacing: -0.5px;
    font-family: 'Playfair Display', serif;
}
</style>
""", unsafe_allow_html=True)

# Admin section
st.markdown("""
<style>
.stExpander {
    background-color: #8B7355 !important;
    border-radius: 12px;
    padding: 1rem;
    margin-top: 2rem;
}
.stExpander > div > div {
    color: #2c3e50 !important;
    font-size: 2.8rem !important;
    font-weight: 600 !important;
    background-color: #8B7355 !important;
}
.stExpander > div > div:hover {
    background-color: #9B8365 !important;
}
.stExpander > div > div > div {
    background-color: #8B7355 !important;
}
.stExpander > div > div > div:hover {
    background-color: #9B8365 !important;
}
.stDataFrame {
    background-color: white;
    border-radius: 8px;
    padding: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Focus styles
st.markdown("""
<style>
*:focus {
    outline: none !important;
    box-shadow: none !important;
}
.stTextInput > div > div > input:focus {
    border-color: #8B7355 !important;
    box-shadow: none !important;
    outline: none !important;
}
.stButton > button:focus {
    border-color: #8B7355 !important;
    box-shadow: none !important;
    outline: none !important;
}
.stExpander > div > div:focus {
    border-color: #8B7355 !important;
    box-shadow: none !important;
    outline: none !important;
}
</style>
""", unsafe_allow_html=True)

# Horizontal lines
st.markdown("""
<style>
hr {
    border-color: #8B7355;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# ===== Header Section =====
# Company Logo
st.markdown(
    f'<div style="text-align: center; margin-bottom: 0.5rem;">'
    f'<img src="data:image/png;base64,{logo_base64}" style="width:300px; display:inline-block; filter: drop-shadow(0px 4px 6px rgba(0, 0, 0, 0.1));">'
    '</div>',
    unsafe_allow_html=True
)

# Profile Picture
st.markdown(
    f'<div style="text-align: center; margin-bottom: 0.5rem;">'
    f'<img src="data:image/jpeg;base64,{profile_base64}" style="width:280px; height:280px; object-fit:cover; border-radius:50%; border: 4px solid #ffffff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); display:inline-block;">'
    '</div>',
    unsafe_allow_html=True
)

# Name and Title
st.markdown('<div class="name">Justin Guthrie</div>', unsafe_allow_html=True)
st.markdown('<div class="title">Geospatial ML/AI Engineer</div>', unsafe_allow_html=True)

# ===== Links Section =====
st.markdown("""
    <a href="https://www.linkedin.com/in/justinmguthrie/" class="link-button" target="_blank">
        Connect with me on LinkedIn
    </a>
    <a href="https://www.enodia.ai" class="link-button" target="_blank">
        Visit our Company Website
    </a>
    <a href="https://calendly.com/d/cwxs-fy8-78n/learn-more-about-our-product-here" class="link-button" target="_blank">
        Schedule a Meeting with Me
    </a>
    """, unsafe_allow_html=True)

# ===== Email Capture Section =====
st.markdown('<div class="stay-connected">Stay Connected</div>', unsafe_allow_html=True)
st.markdown('<div class="email-label">Enter your email for a one page product summary</div>', unsafe_allow_html=True)
email = st.text_input("", label_visibility="collapsed")
if st.button("Subscribe"):
    if email:
        # Create emails directory if it doesn't exist
        if not os.path.exists('emails'):
            os.makedirs('emails')
            
        # Create or load the CSV file
        csv_file = 'emails/subscribers.csv'
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create new entry
        new_entry = pd.DataFrame({
            'email': [email],
            'timestamp': [timestamp]
        })
        
        # Append to existing file or create new one
        if os.path.exists(csv_file):
            new_entry.to_csv(csv_file, mode='a', header=False, index=False)
        else:
            new_entry.to_csv(csv_file, index=False)
            
        st.success("Thank you for subscribing!")
    else:
        st.error("Please enter a valid email address.")

# ===== Admin Section =====
st.markdown("---")
with st.expander("Admin View"):
    password = st.text_input("Enter admin password", type="password")
    if password == os.getenv("ADMIN_PASSWORD"):
        csv_file = 'emails/subscribers.csv'
        if os.path.exists(csv_file):
            df = pd.read_csv(csv_file)
            st.write(f"Total subscribers: {len(df)}")
            st.dataframe(df)
            
            # Download button for the CSV
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download Subscribers CSV",
                data=csv,
                file_name="subscribers.csv",
                mime="text/csv"
            )
        else:
            st.info("No subscribers yet.") 