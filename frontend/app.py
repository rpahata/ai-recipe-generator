import streamlit as st
import requests
from datetime import datetime
from fpdf import FPDF

st.set_page_config(
    page_title="AI Recipe Generator",
    page_icon="🍳",
    layout="centered"
)

# -----------------------------
# DARK MODE TOGGLE
# -----------------------------
dark_mode = st.toggle("🌙 Dark Mode")

if dark_mode:
    st.markdown(
        """
        <style>
        body { background-color: #0e1117; color: white; }
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# TITLE
# -----------------------------
st.title("🍳 AI Recipe Generator Pro")
st.write("Generate recipes, save history, and download PDFs.")

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "selected_ingredients" not in st.session_state:
    st.session_state.selected_ingredients = []

# -----------------------------
# QUICK INGREDIENT BUTTONS
# -----------------------------
st.subheader("🥕 Quick Ingredients")

common_ingredients = ["Chicken", "Rice", "Onion", "Egg", "Garlic", "Tomato"]

cols = st.columns(len(common_ingredients))

for i, ing in enumerate(common_ingredients):
    with cols[i]:
        if st.button(ing):

            if ing not in st.session_state.selected_ingredients:
                st.session_state.selected_ingredients.append(ing)

# -----------------------------
# CLEAR BUTTON
# -----------------------------
if st.button("🧹 Clear Ingredients"):
    st.session_state.selected_ingredients = []

# -----------------------------
# INPUT FIELD
# -----------------------------
ingredients = st.text_area(
    "Enter ingredients",
    value=", ".join(st.session_state.selected_ingredients),
    placeholder="e.g. chicken, rice, onion"
)

# -----------------------------
# GENERATE BUTTON
# -----------------------------
if st.button("🔥 Generate Recipe"):

    if not ingredients.strip():
        st.warning("Please enter ingredients")
    else:
        with st.spinner("👨‍🍳 Cooking your recipe..."):

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/generate-recipe",
                    json={"ingredients": ingredients}
                )

                data = response.json()
                recipe = data.get("recipe", "")

                # save history
                st.session_state.history.append({
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "ingredients": ingredients,
                    "recipe": recipe
                })

                st.success("Recipe generated!")

                # -----------------------------
                # RECIPE CARD UI
                # -----------------------------
                st.markdown("## 🍽️ Recipe Card")

                st.markdown(
                    f"""
                    <div style="
                        padding:20px;
                        border-radius:15px;
                        background-color:#262730;
                        color:white;
                        box-shadow:0px 4px 10px rgba(0,0,0,0.3);
                    ">
                    {recipe.replace('\n', '<br>')}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # -----------------------------
                # PDF DOWNLOAD
                # -----------------------------
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, recipe)

                pdf_file = "recipe.pdf"
                pdf.output(pdf_file)

                with open(pdf_file, "rb") as f:
                    st.download_button(
                        "📥 Download Recipe PDF",
                        f,
                        file_name="recipe.pdf"
                    )

            except Exception as e:
                st.error(f"Error: {e}")

# -----------------------------
# HISTORY SECTION
# -----------------------------
st.markdown("---")
st.subheader("📜 Recipe History")

for item in reversed(st.session_state.history):

    st.markdown(f"**🕒 {item['time']}**")
    st.markdown(f"🥕 {item['ingredients']}")
    st.text(item['recipe'])
    st.markdown("---")