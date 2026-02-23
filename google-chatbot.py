import google.generativeai as genai 

api_key = "AIzaSyB8FoMubgD2EMNjtAiMv64MpO43QsidOI4"
MODEL =  "gemini-3-flash-preview"

SYSTEM_PROMPT = """
ROLE: Act as an expert Technical Resume Writer and Recruiter for AI/ML and Software Engineering roles.

TASK: Create a professional, ATS-optimized resume for internships or entry-level software and AI/ML positions.

INPUT:
Name: Mizba
Education: 3rd Year Engineering Student
Experience: AI/ML and Software Development projects
OUTPUT:
One-page resume with Summary, Skills, Projects, and Education.
Strong action verbs, technical focus, and professional formatting.
INSTRUCTION:
Do not invent fake information; use placeholders if needed.
"""

def setup():
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name=MODEL, system_instruction=SYSTEM_PROMPT)
    chat = model.start_chat(history=[])
    return chat
def ask_ai_stream(chat, message:str)->str:
    response = chat.send_message(message, stream=True)
    full_reply=""
    for chunk in response:
        print(chunk.text,end="",flush=True)
        full_reply+=chunk.text
    print("\n")
    return full_reply
chat = setup()
while True:
    user_input=input("you:").strip()
    ask_ai_stream(chat,user_input)

