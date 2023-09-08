
import openai
import fitz


def extract_text_from_pdf_single(pdf_path):
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

def chat_interface_single(extracted_text):
    user_input = (" 1 What are the drugs given to the patient?"
                  " 2 What side effects were experienced by the patient after he started taking the drugs ? What was the diagnosis?"
                  " 3 Which drug was responsible for the side effect experienced by the patient? Which sentences demonstrate the causality between the drug and the side effect?"
                  " 4 Are any of the identified side effects listed/known?"
    )
    prompt = f""" Mention all the answers case wise for example 
            que: '''{user_input}'''
            data: '''{extracted_text}'''
    """
    response = get_completion(prompt)
    return response
