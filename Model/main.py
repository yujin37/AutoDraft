from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from typing import Optional
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
# 모델 함수 가져오기
from style_model import style_function
from title_model import title_function
from summary_model import summary_function
from blog_model import blog_function

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서 요청을 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"Hello": "World"}

class StyleRequest(BaseModel):
    input_text: str

class TitleRequest(BaseModel):
    input_text: str

class SummaryRequest(BaseModel):
    input_text: str

class BlogRequest(BaseModel):
    topic: str
    input_text: str
    user: str

# style model
@app.post("/style")
def get_style_result(request: StyleRequest):
    """
    Style 모델 호출 API
    """
    result = style_function(request.input_text)
    return {"result": result}

# title model
@app.post("/title")
def get_title_result(request: TitleRequest):
    """
    Title 모델 호출 API
    """
    result = title_function(request.input_text)
    return {"result": result}

# summary model
@app.post("/summary")
def get_summary_result(request: SummaryRequest):
    """
    Summary 모델 호출 API
    """
    result = summary_function(request.input_text)
    return {"result": result}

# blog model
@app.post("/blog")
def get_blog_result(request: BlogRequest):
    """
    Blog 모델 호출 API
    """
    result = blog_function(request.input_text, request.topic, request.user)
    return {"result": result}

# 서버 실행을 위한 코드 (FastAPI 실행 명령어)
if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)