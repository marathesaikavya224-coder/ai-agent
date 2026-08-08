import os
import json
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

# 100% Free via Groq (Loaded securely from environment variables)
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

app = FastAPI(title="AI Cohort Interview Agent API", version="1.0.0")

SESSION_DB = {}

class InterviewRequest(BaseModel):
    session_id: str
    candidate_id: str
    message: Optional[str] = None

class InterviewResponse(BaseModel):
    session_id: str
    status: str
    agent_response: str
    metadata: Dict[str, Any]

INTERVIEWER_PROMPT_TEMPLATE = """You are an expert AI Engineering Hiring Manager conducting a technical interview for a graduate of "The AI Cohort".

Candidate Context:
- Candidate ID: {candidate_id}
- Profile / Signals: Standard AI Engineering student progression
- Completed Missions: Core architectural implementations

Current Interview State:
- Questions Asked Count: {questions_asked_count}
- Curriculum Days Covered: {days_covered}

Rules:
1. Assess the candidate's mastery based on their profile and the curriculum.
2. Ask ONE sharp, conversational question at a time. Drill down into architectural trade-offs.
3. If 'questions_asked_count' < 8, you MUST continue asking relevant technical questions.
"""

@app.post("/api/v1/interview", response_model=InterviewResponse)
def conduct_interview(payload: InterviewRequest):
    try:
        session_id = payload.session_id
        candidate_id = payload.candidate_id
        
        if session_id not in SESSION_DB:
            SESSION_DB[session_id] = {
                "candidate_id": candidate_id,
                "history": [],
                "questions_asked_count": 0,
                "days_covered": []
            }
            
            initial_greeting = (
                "Hello! Welcome to your technical exit interview for The AI Cohort. "
                "Let's dive right in: Walk me through the core architectural decisions and trade-offs you made during your implementation of your core systems."
            )
            SESSION_DB[session_id]["history"].append({"role": "assistant", "content": initial_greeting})
            SESSION_DB[session_id]["questions_asked_count"] = 1
            SESSION_DB[session_id]["days_covered"] = ["Day_01"]
            
            return InterviewResponse(
                session_id=session_id,
                status="in_progress",
                agent_response=initial_greeting,
                metadata={
                    "questions_asked_count": 1,
                    "days_covered": SESSION_DB[session_id]["days_covered"],
                    "interview_complete": False
                }
            )

        session_state = SESSION_DB[session_id]
        history = session_state["history"]

        if payload.message:
            history.append({"role": "user", "content": payload.message})
            session_state["questions_asked_count"] += 1

        q_count = session_state["questions_asked_count"]
        is_complete = q_count >= 8

        system_content = INTERVIEWER_PROMPT_TEMPLATE.format(
            candidate_id=candidate_id,
            questions_asked_count=q_count,
            days_covered=session_state["days_covered"]
        )
        
        messages = [{"role": "system", "content": system_content}] + history
        response = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=messages, temperature=0.6)
        agent_reply = response.choices[0].message.content
        
        history.append({"role": "assistant", "content": agent_reply})

        return InterviewResponse(
            session_id=session_id,
            status="completed" if is_complete else "in_progress",
            agent_response=agent_reply,
            metadata={
                "questions_asked_count": q_count,
                "days_covered": session_state["days_covered"],
                "interview_complete": is_complete
            }
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))