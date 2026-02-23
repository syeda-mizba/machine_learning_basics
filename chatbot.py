import ollama
SYSTEM_PROMPT = """"help me build a resume. my name is mizba and I am CS engineering student """
chat_convo=[]
def chat_with_ollama():
    print("Welcome to")
    while True:
        try:
            user_input=input("User:").strip()
        except(KeyboardInterrupt,e):
            print("User quit")
        chat_convo.append({
            'role':'user',
            "content":user_input
        })
        try:
            print("Chabot prompt started")
            response=ollama.chat(model="phi3:mini",
                                 messages=chat_convo,
                                 options={"system":SYSTEM_PROMPT})
            chat_convo.append({
                'role':'bot',
                "content":response
            })
            print(response)
        except:
            print("Error")
chat_with_ollama()