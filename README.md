# 🛒 Smart Cart Agent System – IKEA Checkout Assistant

An intelligent multi-agent system built with Google's AI Agent Framework (ADK) to enhance the IKEA checkout experience. This root agent coordinates specialized sub-agents to analyze the cart, recommend services, upsell items, optimize shipping costs, and manage delivery scheduling.

---

## 🧠 Overview

The **Smart Cart Agent** is an AI-powered orchestration system designed for IKEA customers. It helps optimize the purchase journey by:

- Identifying service-eligible items
- Recommending relevant services (e.g., assembly, installation)
- Suggesting upsell opportunities
- Offering optimized delivery options
- Scheduling preferred delivery slots
- Reducing total shipping costs via cart optimization

---

## 🧩 Architecture

The system is built using the [Google ADK](https://ai.google.dev) framework with the `gemini-2.0-flash` model. It includes:

### ✅ Root Agent: `service_coordinator_agent`
Coordinates the execution of all sub-agents and manages the user session.

### 🔗 Sub-Agents
| Agent                     | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| `cart_analyzer_agent`     | Detects service-eligible items in the user's cart                      |
| `service_matcher_agent`   | Maps appropriate services to eligible items                            |
| `rag_agent`               | Supplies contextual information from IKEA’s internal knowledge base    |
| `upsell_recommender_agent`| Recommends additional services or products                             |
| `scheduling_and_delivery_agent` | Presents delivery slots and confirms scheduling             |
| `optimizer_agent`         | Suggests cart improvements for cost savings or added value             |

---

## 🏁 Flow Summary

1. **Customer initiates checkout.**
2. `cart_analyzer_agent` checks for eligible items.
3. `service_matcher_agent` proposes services.
4. `rag_agent` enhances recommendations with knowledge base.
5. `upsell_recommender_agent` suggests relevant add-ons.
6. `scheduling_and_delivery_agent` coordinates delivery slots.
7. `optimizer_agent` fine-tunes the cart.
8. `service_coordinator_agent` summarizes all actions to the user.

---

## 🚀 Getting Started

### 1. Clone the repository:
```bash
git clone https://github.com/ingka-group-digital/cart-multi-agent.git
cd smart-cart-agent

Install dependencies:
pip install -r requirements.txt

Create a .env file:
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=ingka-commerce-agenticai-dev
GOOGLE_CLOUD_LOCATION=us-central1
MODEL=gemini-2.0-flash-001
GOOGLE_CLOUD_STAGING_BUCKET=gs://agenticai-services-coordinator

 Start the agent session:
adk web