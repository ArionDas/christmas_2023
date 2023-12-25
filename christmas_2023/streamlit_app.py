from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION_SANTA = ASSETS / "animated_santa.json"
LOTTIE_ANIMATION_CHIMES = ASSETS / "christmas_chimes.json"
LOTTIE_ANIMATION_TREE = ASSETS / "christmas_tree_animation.json"

# Function to load and display the animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
    
# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=7, animation_length="infinite")
    #rain(emoji="🎄", font_size=20, falling_speed=7, animation_length="infinite")
    #rain(emoji="🍩", font_size=20, falling_speed=7, animation_length="infinite")
    
    
# Page configuration
st.set_page_config(page_title="Merry Christmas", page_icon="🎅")

# Run snowfall animation
run_snow_animation()

# Applying custom css
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
# Page header
st.header(f"Merry Christmas!!",anchor=False)    

# Displaying the lottie animation
col1, col2, col3 = st.columns(3)
lottie_animation_1 = load_lottie_animation(LOTTIE_ANIMATION_SANTA)
#st_lottie(lottie_animation_1, key="lottie_holiday_1", height=300)

lottie_animation_2 = load_lottie_animation(LOTTIE_ANIMATION_TREE)
#st_lottie(lottie_animation_2, key="lottie_holiday_2")

lottie_animation_3 = load_lottie_animation(LOTTIE_ANIMATION_CHIMES)
#st_lottie(lottie_animation_3, key="lottie_holiday_3", height=300)

with col1:
    st_lottie(lottie_animation_1, key="lottie_holiday_1")
with col2:
    st_lottie(lottie_animation_2, key="lottie_holiday_2")
with col3:
    st_lottie(lottie_animation_3, key="lottie_holiday_3")

# Displaying the personal message
st.markdown (
    f"<h4>Merry Christmas and warmest holiday wishes to you and your cherished family! May this festive season wrap you in the joy of togetherness and fill your hearts with the magic of love.</h4>",
    unsafe_allow_html=True
)

markdown_text = "Made with 💖 by [Arion](https://www.linkedin.com/in/arion-das/)"
st.markdown (
    markdown_text,
    unsafe_allow_html=True
)

