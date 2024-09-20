**Negotiation Chatbot using Google Flan-T5 Model**
This repository contains a Negotiation Chatbot that leverages the Google Flan-T5 Large model for natural language conversation and intent-based price negotiation. The chatbot facilitates negotiation on products like smartphones, laptops, and electronics, with a focus on guiding users through product inquiry and pricing discussions.

Key Features
Product Inquiry: The chatbot engages in multi-turn conversations with users to collect details about the product (e.g., brand, model, color) and then presents the base price of the product.
Price Negotiation: The chatbot initiates price negotiations after the product details are provided, allowing the user to request discounts, and offers step-by-step counter-discounts.
Dynamic Conversation Flow: The chatbot simulates a realistic negotiation flow, managing multi-turn dialogues until a final price agreement is reached.
Natural Language Processing: Utilizes the Google Flan-T5 model for response generation and Sentence-BERT for detecting user intent (e.g., product inquiry, price negotiation).
API-Driven Interaction: Built as a Flask-based REST API, it can be tested through curl commands or Postman.
How It Works
Conversation Initialization: The chatbot starts by asking the user for their desired product (e.g., "What kind of phone do you want?").
Product Details Collection: It collects the necessary details like brand, model, and color.
Price Disclosure: The chatbot shares the base price of the product.
Negotiation Process: Users can negotiate by requesting discounts. The bot offers a predefined discount percentage (e.g., 5%, 7%) and closes the deal when an agreement is reached.
Deal Closure: Once a price is settled, the chatbot confirms the deal and ends the conversation.
Tech Stack
Google Flan-T5 (Large Model): For generating natural, conversational responses based on user input.
Sentence-BERT (all-MiniLM-L6-v2): To detect user intents like product inquiry, negotiation, and exit.
Flask: A lightweight web framework used for creating API endpoints.
Python: Language used to integrate the model, manage conversation history, and handle negotiation logic.
