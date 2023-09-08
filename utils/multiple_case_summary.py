
import openai
import fitz


def extract_text_from_pdf_multiple(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf_document:
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
    return text

def get_completion(prompt, model="gpt-3.5-turbo-16k"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # Adjust the temperature as needed
    )
    return response.choices[0].message["content"]

def chat_interface_multiple(extracted_text):
    user_input=("Give me the List of drugs according to case wise?",
                "Which demonstrate the causality between the drug and the side effect according to case wise ?",
                "what is the side effect the patient experienced? Which drug was responsible for it?"
)
    prompt = f""" Mention all the answers case wise for example
        case 1:
            answer all three questions
        case 2:
            answer all three questions
        que:'''{user_input}''' 
        data: '''{extracted_text}'''
        """
    response = get_completion(prompt)
    return response
