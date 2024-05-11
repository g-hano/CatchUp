# CatchUp
CatchUp is developed by the winner of AI'NTEP Hackathon, Ketçap team.

## Overview
The CatchUp is an innovative AI-driven application designed to identify the best products for various countries. Developed using ChatGPT 3.5 Turbo and hosted on Streamlit, this tool leverages advanced natural language processing to analyze and recommend products based on localized data and preferences. This project was awarded first place in a prestigious AI competition, highlighting its effectiveness and innovation.

## Features
- **AI-Powered Recommendations**: Utilizes the latest in AI technology to provide tailored product suggestions.
- **Multi-Country Analysis**: Capable of handling queries for a list of different countries, providing specific insights per region.
- **Interactive Web Interface**: Hosted on Streamlit, offering a user-friendly and responsive interface for users to interact with the AI.
- **Robust Tool Integration**:
  - **Report Tool**: Saves the final version of the analysis report.
  - **Internet Search Tool**: Gathers data from various online sources via a Search Engine API.
  - **Wikipedia Search Tool**: Delivers detailed information from Wikipedia for scientific or specific queries.

## Tools Used
- Streamlit (`st`)
- Llama Index Libraries:
  - `ReActAgent`
  - `FunctionTool`
  - `ChatMemoryBuffer`
  - `Ollama`
  - `OpenAI`
- Custom Tools:
  - `Report`
  - `InternetSearch`
  - `wikipedia_search`

## Getting Started

### Prerequisites
Ensure you have Python installed on your machine. The application is built using Python and requires Python 3.11.3

```
git clone https://github.com/g-hano/CatchUp
pip install -r requirements.txt
streamlit run main.py
```
Access the web interface by visiting:
https://ketcap-catchup.streamlit.app/

## Developer Team
* [Elif Nisa Ölçücü](https://www.linkedin.com/in/elif-nisa-%C3%B6l%C3%A7%C3%BCc%C3%BC-08984023b/)
* [Cihan Yalçın](https://www.linkedin.com/in/chanyalcin/)
* [Fatma Betül Avcı](https://www.linkedin.com/in/fatma-bet%C3%BCl-avc%C4%B1-926b39254/)
* [Ebrar Özer](https://www.linkedin.com/in/ebrar-%C3%B6zer-763699207/)
