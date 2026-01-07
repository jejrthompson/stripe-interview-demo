# Stripe SA Tech Screen Prep

Interview prep for Solutions Architect, Enterprise technical screen at Stripe.

**Interview Date:** Wednesday, January 7, 2026 at 10:00 AM PT  
**Interviewer:** Kelly Chang (Senior Solutions Architect)  
**Duration:** 45 minutes  
**Format:** Two parts - API familiarity (15 min) + System Design (20 min) + buffer/Q&A (~10 min)

---

## Quick Start

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your Stripe test keys

# Launch Jupyter
jupyter notebook
```

---

## Project Structure

```
stripe-sa-prep/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── notebooks/
│   └── part1_stripe_connect.ipynb    # On-demand delivery with Connect
├── docs/
│   └── part2_system_design.md        # Maps.co reverse API design
└── diagrams/
    ├── part1/                        # Connect flow diagrams
    └── part2/                        # System design diagrams
```

---

## Part 1: On-Demand Delivery Service (15 min)

Build a DoorDash-style platform with Stripe Connect.

### The Players

| Party | Role | Stripe Representation |
|-------|------|----------------------|
| Platform | Delivery service (you) | Main Stripe account |
| Restaurant | Provides food | Custom Connected Account |
| Courier | Delivers food | Custom Connected Account |
| Customer | Pays for order | Customer object |

### Three Deliverables

1. **Onboard** restaurant and courier using Custom account type
   - Explain steps involved (no need to demo live onboarding)
   - Discuss purpose and importance of onboarding process

2. **Collect payment** from customer
   - Describe how to collect payment information
   - Demonstrate API calls and Stripe features to create the payment

3. **Route funds** using Separate Charges & Transfers
   - Walk through the funds flow
   - Demonstrate API calls to route funds
   - Discuss edge cases and additional requirements

### Money Flow Example ($35 order)

```
Customer pays $35.00
    │
    ▼
Platform Stripe Balance ($35.00)
    │
    ├── Transfer $25.00 ──► Restaurant (food cost)
    ├── Transfer $7.00  ──► Courier (delivery fee)
    └── Keep $3.00      ──► Platform (service fee)
```

---

## Part 2: System Design - Reverse API (20 min)

**Full spec:** [docs/part2_system_design.md](docs/part2_system_design.md)

**Scenario:** You're a PM at Maps.co (like Google Maps). You've partnered with food delivery companies (Food.co = Uber Eats/DoorDash). Users can order food directly in the Maps app. Food.co partners will implement your "reverse API" - you define the contract, they host the endpoints.

### Deliverables

1. **High-level architecture diagram** - Maps.co ↔ Food.co communication patterns
2. **Reverse API endpoints** - What Food.co must implement (restaurants, menu, orders)
3. **Webhooks** - What Maps.co exposes for async updates (order status, driver location)

---

## Edge Cases to Prepare For

- Refunds (full and partial)
- Courier no-show / failed delivery
- Restaurant out of stock mid-order
- Disputes and chargebacks
- Multi-currency considerations
- Payout timing (instant vs standard)

---

## Resources

- [Stripe Connect Documentation](https://stripe.com/docs/connect)
- [Custom Accounts](https://stripe.com/docs/connect/custom-accounts)
- [Separate Charges and Transfers](https://stripe.com/docs/connect/charges-transfers)
- [Connect Testing](https://stripe.com/docs/connect/testing)
- [Payment Intents API](https://stripe.com/docs/api/payment_intents)
- [Transfers API](https://stripe.com/docs/api/transfers)

---

## FarmShare Experience Reference

Prior implementation context to draw from:

- Built Stripe Connect marketplace for vendor payouts
- WooCommerce integration for consumer marketplace
- Custom B2B platform using Stripe SDK (Node.js)
- Products, Subscriptions, Invoices, Taxes modules
- Real money flowing to real vendors in production

---

## Interview Tips

- Keep Part 1 to ~12-13 min to leave buffer for questions
- Use diagrams, Stripe docs, or live API calls to illustrate solutions
- Use Jupyter to show live API calls with visible request/response
- Have Stripe Dashboard open in test mode as backup
- Collapse output cells until needed for cleaner navigation
- Speak from FarmShare experience - you've done this for real
- Be prepared to explain decision-making and address follow-up questions
