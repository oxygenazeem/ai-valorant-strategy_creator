import streamlit as st
from g4f.client import Client

# Set up page layout for a dedicated Valorant Coach
st.set_page_config(page_title="Valorant Strategy Coach", layout="centered")
st.title("Valorant Strategy Coach")
st.write("Get instant tactical adjustments, ability setups, and lurk timings.")

# Initialize the unlimited free client
client = Client()

# 1. Dedicated Valorant Inputs
col1, col2 = st.columns(2)

with col1:
    agent = st.text_input("Your Agent (e.g., Cypher, Jett, Omen)", placeholder="Enter Agent...")
    map_name = st.text_input("Map (e.g., Bind, Ascent, Lotus)", placeholder="Enter Map...")

with col2:
    side = st.radio("Current Side", ["Attacking", "Defending"])

# Extra situational details to give the AI more context
scenario = st.text_input(
    "Specific Scenario / Matchup (Optional)", 
    placeholder="e.g., Enemy team has an aggressive Jett operator, or holding A site solo"
)

# 2. Build the tailored Valorant prompt
prompt = f"""
Act as an Immortal-ranked Valorant Coach. Provide an elite tactical strategy breakdown for playing {agent} on the map {map_name} while on the {side} side.
"""

if scenario:
    prompt += f"\nSpecifically factor in this matchup context: {scenario}."

prompt += "\n\nProvide 3 specific, high-impact tactical tips focusing strictly on ability usage, positioning, or rotation timings. Keep the tone aggressive, tactical, and highly competitive."

# 3. Trigger button
if st.button("Generate Tactical Breakdown"):
    if agent and map_name:
        with st.spinner(f"Analyzing meta data for {agent} on {map_name}..."):
            try:
                # Fire the request out to the free endpoint
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}],
                )
                
                st.subheader("Tactical Breakdown")
                st.write(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"Error generating tactics: {e}")
    else:
        st.warning("Please fill in both the Agent and Map fields first!")