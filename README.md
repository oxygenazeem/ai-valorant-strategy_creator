# Valorant Strategy Program Powered by Artificial Intelligence
An interactive web application built with Python and Streamlit that acts as a high-tier Valorant coach. It provides instant, context-specific tactical breakdowns, ability setups, and map macro tips based on your chosen Agent, Map, Side, and optional custom matchups.

By utilizing the g4f library, this tool runs entirely on free, open-source routing endpoints—meaning zero API keys, zero limits, and 100% free hosting.

## Features

* Dedicated Valorant Focus: Tailored strictly for high-level tactical adjustments (Attacking/Defending).
* Dynamic Scenario Injection: Add custom matchup details (e.g., "Enemy Jett is holding A Main with an Operator") to get tailored counters.
* No API Key Restrictions: Skips standard developer daily limits entirely via automated endpoint routing.
* Streamlit Interface: A clean, responsive user UI accessible via desktop or mobile web browsers.

## Local Setup Instructions

If you want to clone this repository and run this project locally on your machine, follow these steps:
Clone the Repository:
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
Change directory:
cd YOUR_REPO_NAME
Install Requirements:
pip install -r requirements.txt
Run the App:
streamlit run ai_gamingStrategy.py

## Cloud Deployment

This repository is fully optimized to be deployed for free on Streamlit Community Cloud:
The requirements.txt file is pre-configured for automated cloud server installation.
No hidden variables or keys are required, ensuring instant, seamless builds.

## Tech Stack

- Frontend UI: Streamlit
- AI Engine: g4f (Client routing for GPT-4o architecture)
- Language: Python 3
