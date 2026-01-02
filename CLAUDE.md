# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Stripe Solutions Architect interview preparation project. Contains Jupyter notebooks demonstrating Stripe Connect API usage for a DoorDash-style on-demand delivery platform.

## Development Commands

```bash
# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add Stripe test keys

# Run Jupyter
jupyter notebook
```

## Architecture

**Stripe Connect marketplace pattern** with three parties:
- **Platform** (main Stripe account) - the delivery service
- **Connected Accounts** (Custom type) - restaurants and couriers
- **Customers** - end users paying for orders

**Payment flow uses Separate Charges & Transfers:**
1. Customer payment hits platform's Stripe balance
2. Platform transfers portions to connected accounts (restaurant, courier)
3. Platform retains service fee

## Key Stripe APIs

- Connect Custom Accounts for onboarding restaurants/couriers
- Payment Intents for collecting customer payments
- Transfers API for routing funds to connected accounts
