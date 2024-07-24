---
title: Skeduler
emoji: 💬
colorFrom: yellow
colorTo: purple
sdk: gradio
sdk_version: 4.36.1
app_file: app.py
pinned: false
---

---

# Chatbot with Gradio and Hugging Face Inference API

This project implements a chatbot using the Gradio interface and the Hugging Face Inference API. The chatbot is designed to help users book appointments and find the nearest locations using the Skeduler service.

## Features

- **Conversational Interface**: The chatbot engages users in a friendly and helpful manner.
- **Customizable Parameters**: Adjust the system message, maximum tokens, temperature, and top-p settings for generating responses.
- **Streaming Responses**: The chatbot streams its responses token by token for a more dynamic user experience.


### Code Explanation

1. **Imports and Initialization**

    ```python
    import gradio as gr
    from huggingface_hub import InferenceClient
    ```

    Import necessary libraries and initialize the Hugging Face Inference Client with the specified model.

2. **Respond Function**

    The `respond` function handles the conversation logic. It sets up a system message, constructs a list of messages, appends the new user message, and streams the response from the model.

    ```
    def respond(
        message,
        history: list[tuple[str, str]],
        system_message,
        max_tokens,
        temperature,
        top_p,
    ):
        system_message = "Booking appointments now easier than ever..."
        messages = [{"role": "system", "content": system_message}]

        for val in history:
            if val[0]:
                messages.append({"role": "user", "content": val[0]})
            if val[1]:
                messages.append({"role": "assistant", "content": val[1]})

        messages.append({"role": "user", "content": message})

        response = ""

        for message in client.chat_completion(
            messages,
            max_tokens=max_tokens,
            stream=True,
            temperature=temperature,
            top_p=top_p,
        ):
            token = message.choices[0].delta.content
            response += token
            yield response
    ```

3. **Gradio Interface**

    The Gradio interface is set up with the `respond` function and additional inputs for customizing the chatbot's behavior.

    ```
    demo = gr.ChatInterface(
        respond,
        additional_inputs=[
            gr.Textbox(value="You are a friendly Chatbot.", label="System message"),
            gr.Slider(minimum=1, maximum=2048, value=512, step=1, label="Max new tokens"),
            gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
            gr.Slider(
                minimum=0.1,
                maximum=1.0,
                value=0.95,
                step=0.05,
                label="Top-p (nucleus sampling)",
            ),
        ],
    )
    ```

4. **Launching the Interface**

    Launch the Gradio interface to make the chatbot available for interaction.

    ```
    if __name__ == "__main__":
        demo.launch()
    ```

---
