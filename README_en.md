# AutoDraft  

## Project Overview  
AutoDraft is a service designed for the **era of personal PR**, enabling effective content creation for diverse SNS platforms such as Facebook, Instagram, LinkedIn, Slack, and Discord.  
While community engagement becomes increasingly important, content creation often feels burdensome.  
AutoDraft simplifies this process by providing an all-in-one solution for **content generation, title suggestion, hashtag recommendation, and content summarization**.  

## Getting Started  

### Requirements  
For building and running the application, you need:  
- Python 3.8 or higher  
- pip or Poetry  
- Node.js (if required for frontend development)  

### Installation  

#### Backend  
1. Install FastAPI:  
   ```bash
   pip install fastapi uvicorn
    ```
2. Install additional dependencies
```bash
pip install -r requirements.txt
```
3. Start the FastAPI server
```bash
uvicorn main:app --reload
```
#### Frontend
1. Install Streamlit:
```bash
pip install streamlit
```
2. Start the Streamlit app:
```bash
streamlit run app.py
```
## 화면 구성
## 주요 기능
- Content Generation

    - Create content by reflecting previously inputted user characteristics
- Hashtag Recommendation

    - Maximize visibility on SNS by recommending hashtags associated with input content.
- Content Title

    - Recommended attractive content titles through user input.
- Content Summary

    - Provides concise and key information by summarizing long content.



## 아키텍처 
