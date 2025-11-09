from google import genai
from google.genai import types
import os
import sys
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not loaded. Check your .env and working directory.")

client = genai.Client(api_key=api_key)



def main():
    if len(sys.argv)<=1:
        print('Error: No prompt provided')
        sys.exit(1)
    args = [a for a in sys.argv[1:] if a != '--verbose']
    question=" ".join(args)
    verbose = '--verbose' in sys.argv
    if verbose:
        print(f'User prompt: {question}')
    messages = [
    types.Content(role='user', parts=[types.Part(text=question)]),]
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages)
    if verbose:
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    print(response.text)



if __name__ == "__main__":
    main()
