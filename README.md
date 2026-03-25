# Promptfoo Learning Guide

Welcome to the Promptfoo learning project! This repository contains a working configuration to help you learn Promptfoo basics, utilizing Google Vertex AI and Python integration.

## What is Promptfoo?
Promptfoo is a CLI and library for evaluating LLM output quality. It allows you to systematically test prompts and models against predefined test cases, ensuring that your LLM applications behave reliably as you change prompts, models, or system parameters.

## Core Concepts to Know
1. **Providers**: The LLM APIs or models you are testing (e.g., Google Vertex AI, Anthropic, OpenAI).
2. **Prompts**: The instructions you send to the LLM. Promptfoo allows you to separate prompts into cleanly separated files (e.g., `prompts.txt`) and inject variables via placeholders like `{{topic}}`.
3. **Tests**: The scenarios you want to evaluate. They primarily consist of `vars` (variable values injected into the prompt) and `assert` statements.
4. **Assertions**: The rules that validate the LLM's output. They can be deterministic string matches (`icontains`, `equals`), LLM-as-a-judge criteria (`llm-rubric`), or custom programmatic rules (like our Python script).

## Setup & Dependencies

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Authenticate with Google Cloud (for Vertex AI):**
   ```bash
   gcloud auth application-default login
   gcloud config set project YOUR_PROJECT_ID
   ```
   Or set the `GOOGLE_APPLICATION_CREDENTIALS` and `GCLOUD_PROJECT` environment variables.

3. **Install Promptfoo:**
   ```bash
   npm install -g promptfoo
   ```

## Project Structure
- `promptfooconfig.yaml`: The main configuration file tying everything together (specifies providers, prompts, and the test cases).
- `prompts.txt`: Contains the raw prompt template.
- `custom_eval.py`: A Python script containing custom assertion logic. During evaluations, Promptfoo executes this to validate the outputs programmatically based on your logic.

## Running Evaluations

To run your tests as configured in `promptfooconfig.yaml`:

```bash
npx promptfoo eval
```
This runs all test cases against the configured providers and outputs a pass/fail summary matrix in your terminal.

## Viewing Results

To see a detailed, interactive web dashboard with your evaluation results, side-by-side prompt comparisons, and assertion reasoning:

```bash
npx promptfoo view
```
