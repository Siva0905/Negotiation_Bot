from flask import Flask, request
from transformers import T5Tokenizer, T5ForConditionalGeneration
from sentence_transformers import SentenceTransformer, util
import torch
#Flask APP
app = Flask(__name__)

#Model's included- T5 Flan and Sentence BERT
model_name = "google/flan-t5-large"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
intent_model = SentenceTransformer('all-MiniLM-L6-v2')

#Intent Classification
intents = ["negotiate price", "inquire about product", "exit"]

def detect_intent(user_input):
    intent_model = SentenceTransformer('all-MiniLM-L6-v2')
    user_embedding = intent_model.encode(user_input, convert_to_tensor=True)
    intent_embeddings = intent_model.encode(intents, convert_to_tensor=True)
    similarity_scores = util.pytorch_cos_sim(user_embedding, intent_embeddings)
    best_intent_idx = similarity_scores.argmax().item()
    return intents[best_intent_idx]

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=100, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

conversation_history = []

def generate_response_with_history(user_input):
    conversation_history.append(f"Customer: {user_input}")
    context = " ".join(conversation_history)
    prompt = f"As a supplier, continue this conversation: {context}"
    response = generate_response(prompt)
    if response not in conversation_history:
        conversation_history.append(f"Supplier: {response}")
        return response
    else:
        return generate_response_with_history(user_input) 
@app.route('/negotiate', methods=['POST'])

def start_negotiation():
    print("Welcome to the negotiation chatbot!")
    base_price = 150  # Example base price
    min_price = 100   # Example minimum price
    discount_percentage = 5  # Initial discount percentage
    final_discount_percentage = 7  # Final discount percentage
    price_offered = False  # Track whether the base price has been offered
    deal_made = False  # Track if a deal has been finalized

    while True:
        user_input = input("Customer: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Negotiation ended.")
            break
        detected_intent = detect_intent(user_input)
        print(f"Detected Intent: {detected_intent}")

        if detected_intent == "inquire about product":
            bot_response = generate_response_with_history(user_input)
            print(f"Supplier: {bot_response}")

            if "color" in user_input.lower() and not price_offered:
                print(f"Supplier: The price for the {user_input.split()[-1]} Samsung Galaxy S21 is {base_price}.")
                price_offered = True

        elif detected_intent == "negotiate price":
            if not deal_made:
                if "can i get a discount" in user_input.lower():
                    print(f"Supplier: We can offer a discount of {discount_percentage}%.")
                    print(f"Supplier: The price after discount is {base_price * (1 - discount_percentage / 100):.2f}.")
                elif "can you give more discount" in user_input.lower():
                    print(f"Supplier: We can finalize the deal at {final_discount_percentage}%.")
                    print(f"Supplier: The final price will be {base_price * (1 - final_discount_percentage / 100):.2f}.")
                elif "alright, ill take it" in user_input.lower():
                    print("Supplier: That's great. Let's end the deal. Thank you!")
                    deal_made = True
                else:
                    print("Please enter a valid negotiation request.")
            else:
                print("The deal has already been closed. Thank you!")

        else:
            print("Goodbye!")
            break

if __name__ == "__main__":
    start_negotiation()





