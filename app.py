import streamlit as st

st.set_page_config(
    page_title="Political Empire",
    page_icon="🗳️",
    layout="wide"
)


# -------------------------
# INITIAL PLAYER
# -------------------------

def init_game():

    if "player" not in st.session_state:

        st.session_state.player = {

            "name": "Shashank",

            "money": 5000,

            "land": 0.50,

            "popularity": 5,

            "trust": 10,

            "supporters": 20,

            "year": 2002,

            "stage": "Student Union Election",

            "turn": 1
        }


init_game()


# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("Player")

p = st.session_state.player

st.sidebar.metric("Money", f"₹{p['money']}")
st.sidebar.metric("Land", f"{p['land']} Acre")
st.sidebar.metric("Popularity", f"{p['popularity']}%")
st.sidebar.metric("Trust", f"{p['trust']}%")
st.sidebar.metric("Supporters", p["supporters"])

st.sidebar.divider()

if st.sidebar.button("Reset Game"):

    del st.session_state.player
    st.rerun()


# -------------------------
# MAIN
# -------------------------

st.title("🗳️ Political Empire")

st.subheader("Ujjain Campaign")

col1, col2 = st.columns(2)

with col1:

    st.info(f"""
**Year**

{p["year"]}

**Stage**

{p["stage"]}

**Turn**

{p["turn"]}/10
""")


with col2:

    st.success("""
Goal

✔ Win Election

✔ Save Maximum Money

✔ Increase Land

✔ Build Popularity
""")


st.divider()

st.header("Current Situation")

st.write(
"""
Bio students are demanding sports equipment before the election.

If you support them, Bio votes will increase,
but your campaign budget will reduce.
"""
)

choice = st.radio(

    "Choose your action",

    [

        "Give Sports Kit (₹1000)",

        "Girls Rally (₹2000)",

        "Posters (₹300)",

        "Ignore Everyone"

    ]
)


if st.button("Confirm Decision"):

    if choice == "Give Sports Kit (₹1000)":

        p["money"] -= 1000
        p["popularity"] += 5
        p["supporters"] += 10

        st.success("Bio students are happy.")

    elif choice == "Girls Rally (₹2000)":

        p["money"] -= 2000
        p["trust"] += 5
        p["popularity"] += 3

        st.success("Girls support increased.")

    elif choice == "Posters (₹300)":

        p["money"] -= 300
        p["popularity"] += 2

        st.success("Campaign visibility increased.")

    else:

        p["trust"] -= 2

        st.warning("Students are unhappy.")

    p["turn"] += 1

    if p["turn"] > 10:

        st.balloons()

        st.success("Election Finished (Result Screen will be added in Commit 002)")

    st.rerun()
