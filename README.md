# AI Procurement Negotiator

## Overview

This repository contains the AI-powered chatbot that automates procurement negotiations. It is inspired by Walmart's case study, where the company implemented AI technology to negotiate with tail-end suppliers and improve procurement processes. The chatbot uses advanced machine learning algorithms to engage in automated negotiations, optimize payment terms, and generate cost savings for businesses.

### Background
Walmart faced the challenge of negotiating with a vast number of suppliers, where traditional methods were inefficient and costly. In 2021, Walmart piloted an AI-powered negotiation solution with Pactum AI that successfully automated negotiations with suppliers for categories such as fleet services and equipment used in stores. The AI chatbot successfully reached agreements with 64% of suppliers in the pilot and generated an average savings of 1.5%, along with an extension of payment terms.

This project demonstrates the potential of AI in procurement, offering key lessons for businesses looking to implement similar systems.

---

## Features

- **Automated Negotiations**: The AI chatbot negotiates payment terms, price discounts, and other procurement conditions with suppliers.
- **Supplier Engagement**: Suppliers can interact with the chatbot at their own pace, making counteroffers and negotiating terms that work for both parties.
- **Savings & Flexibility**: The system helps companies achieve savings and extend payment terms, while offering suppliers greater flexibility in negotiations.
- **Scalable Solution**: This approach can be scaled across various categories and industries for enhanced procurement efficiency.

---

## Case Study Insights

### The Pilot at Walmart

- **Objective**: Automate negotiations with tail-end suppliers, focusing on goods not for resale (e.g., fleet services, carts, store equipment).
- **Results**:
  - **64%** of suppliers agreed to new terms, exceeding the 20% target.
  - Average **savings of 1.5%** on negotiated spend.
  - Payment terms were extended to an average of **35 days**.
- **Supplier Feedback**: 83% of suppliers who successfully negotiated with the chatbot found the process easy to use and appreciated the ability to make counteroffers.

### Key Lessons for Implementing AI in Procurement

1. **Move Quickly to Production**: Instead of lingering in proof-of-concept phases, Walmart focused on business goals and moved directly to a production pilot.
2. **Collaborative Development**: Business owners, procurement specialists, and legal teams worked together to create realistic negotiation scenarios and ensure the system adhered to contracting standards.
3. **Supplier Flexibility**: The AI chatbot was designed to provide flexibility to suppliers, allowing them to negotiate at their own pace, which led to better engagement.

---

## How It Works

1. **Input**: Suppliers are selected based on available data, such as payment terms and opportunity for discounts.
2. **Negotiation Scenarios**: The chatbot engages suppliers using predefined negotiation scripts based on business goals.
3. **Dynamic Responses**: The chatbot processes responses, makes counteroffers, and finalizes agreements.
4. **Output**: The system generates contracts or agreement terms based on the negotiation, which are then reviewed by legal teams if necessary.

---

## Requirements

To use or contribute to this project, the following are required:

- Python 3.7+ 
- Required libraries:
  - `TensorFlow` or `PyTorch` (for machine learning models)
  - `Transformers` (for NLP processing)
  - `Flask` or `FastAPI` (for the chatbot API)
  - `pandas` (for data handling)
  - `scikit-learn` (for training and validation)

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ai-procurement-negotiator.git
    cd ai-procurement-negotiator
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables (optional):
    - For accessing external services (e.g., Pactum API or databases).

4. Run the chatbot locally:
    ```bash
    python run_chatbot.py
    ```

---

## Contributing

We welcome contributions from the community. If you're interested in improving the chatbot or adding new features, please fork the repository, make changes, and submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or suggestions, feel free to reach out to us at [your_email@example.com].

