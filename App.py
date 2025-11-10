import streamlit as st


def bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / (height_m ** 2)


def category(bmi_value: float) -> str:
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"

# --- CSS ---
st.markdown(
    """
    <style>
    .stApp {background-color:#001a33;}
    div[data-testid="stNumberInput"] input {
        background-color:#0b2d52;
        color:#e6e6e6;
        border:1px solid #3a516e;
    }
    .stButton>button{
        background-color:#133c66;
        color:#e6e6e6;
        border:1px solid #3a516e;
    }
    .stMarkdown {
        color:#e9e9e9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("BMI Calculator")

w = st.number_input("Weight (kg)", min_value=0.1, format="%.2f")
h = st.number_input("Height (meters)", min_value=0.1, format="%.2f")

if st.button("Compute"):
    val = bmi(w, h)
    st.write(f"BMI = {val:.2f}")
    st.write("Category:", category(val))

    # number line plot


fig, ax = plt.subplots(figsize=(7, 1.2))
ax.set_xlim(10, 40)
ax.set_ylim(0, 1)

# shade zones (neutral tones — no bright saturation)
ax.axvspan(10, 18.5, alpha=0.25)
ax.axvspan(18.5, 25, alpha=0.15)
ax.axvspan(25, 30, alpha=0.25)
ax.axvspan(30, 40, alpha=0.35)

# marker for actual BMI
ax.axvline(val, linewidth=6)

ax.set_yticks([])
ax.set_xlabel("BMI scale — 10 → 40")

st.pyplot(fig)(fig)
