import streamlit as st

from engine.player import Player
from engine.scenario import ScenarioLoader
from engine.election import Election


st.set_page_config(page_title="Political Empire",layout="wide")


if "player" not in st.session_state:

    st.session_state.player=Player()

if "election" not in st.session_state:

    st.session_state.election=Election()

loader=ScenarioLoader("data/scenarios/student_union_2002.json")

player=st.session_state.player

election=st.session_state.election

turn=player.turn


st.title("🗳 Political Empire")

st.subheader("Student Union Election 2002")


col1,col2=st.columns([1,2])


with col1:

    st.metric("Money",f"₹{player.money}")

    st.metric("Land",player.land)

    st.metric("Popularity",player.popularity)


    st.divider()

    st.write("### Survey")

    st.progress(election.groups["bio"]/100)

    st.caption(f"Bio Support")

    st.progress(election.groups["commerce"]/100)

    st.caption("Commerce Support")

    st.progress(election.groups["arts"]/100)

    st.caption("Arts Support")

    st.progress(election.groups["girls"]/100)

    st.caption("Girls Support")


with col2:

    if turn<=len(loader.data["turns"]):

        scene=loader.get_turn(turn)

        st.header(f"Turn {turn}")

        st.info(scene["issue"])

        option=st.radio(

            "Decision",

            range(len(scene["choices"])),

            format_func=lambda i:scene["choices"][i]["text"]

        )

        if st.button("Confirm Decision"):

            selected=scene["choices"][option]

            cost=election.apply_choice(selected)

            player.money+=cost

            player.turn+=1

            st.rerun()

    else:

        st.success("Election Finished")

        total=sum(election.groups.values())

        st.metric("Estimated Votes",total)

        st.balloons()
