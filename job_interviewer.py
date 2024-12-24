from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

interview_role = {"role": "system", "content": "You are an interviewer named Bob. You will ask questions and then assess the responses, please return only the questions or responses not in quotes."}
assess_role = {"role": "system", "content": "You are an assessor for interview performance. You will evaluate previous responses to the interview questions that you ask and determine the likelihood the interviewee gets the job with the provided responses, identify strengths, and identify areas of improvement, please return only the responses not in quotes."}
responses = []

def line():
    print("--------------------------")

def introduce(job):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[interview_role,
                  {"role": "user", "content": f"I'm applying for this position: {job}. Could you introduce  yourself as an interviewer for this position and then ask me a generic standard interview question?"}]
    )
    return response.choices[0].message.content.strip()

def ask_question(job):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[interview_role,
                  {"role": "user", "content": f"I'm applying for this position: {job}. Could you ask me a common interview question for this position?"}]
    )
    return response.choices[0].message.content.strip()

def assess(job, responses):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[assess_role,
                  {"role": "user", "content": f"I'm applying for this position: {job}. Could you assess my previous responses here and give me an in depth review of how I did, making sure to highlight the likelihood I get the job and areas where I can improve? {responses}"}]
    )
    return response.choices[0].message.content.strip()

def main():
    job = input("Please enter the job you're applying for: ")
    numq = int(input("How many questions would you like me to ask? "))
    line()

    intro = introduce(job)
    print(intro)
    responses.append(input("---> "))

    for i in range(numq):
        question = ask_question(job)
        print("\n" + question)
        responses.append(input("---> "))

    line()

    assess_performance = assess(job, responses)
    print("Assessment:")
    print(assess_performance)

if __name__ == "__main__":
    main()