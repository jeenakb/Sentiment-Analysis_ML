import panel as pn
from openai import OpenAI

pn.extension()

# --- Initialize OpenAI ---
client = OpenAI(api_key="YOUR_KEY")  # replace with your key

# --- Menu and toppings ---
MENU = {
    "burger": 3,
    "pizza": 3,
    "loaded fries": 3
}

TOPPINGS = {
    "alepino": 0.5,
    "cucumber": 0.5,
    "extra cheese": 0.5
}

# --- Store conversation ---
conversation = []

# --- Panel widgets ---
user_input = pn.widgets.TextInput(value="", placeholder="Type your order here...")
send_button = pn.widgets.Button(name="Talk")
chat_area = pn.pane.Markdown("", height=300, sizing_mode="stretch_width")

# --- Function to calculate total ---
def calculate_total(text):
    text = text.lower()
    total = 0
    for item in MENU:
        if item in text:
            total += MENU[item]
    for topping in TOPPINGS:
        if topping in text:
            total += TOPPINGS[topping]
    return total

# --- Function to handle button click ---
def handle_order(event):
    global conversation
    user_text = user_input.value
    if not user_text.strip():
        return

    # --- Call OpenAI ---
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}]
    )
    reply = response.choices[0].message.content

    # --- Calculate total using Python ---
    total = calculate_total(user_text)

    # --- Append to conversation ---
    conversation.append(f"**You:** {user_text}")
    conversation.append(f"**Foodie:** {reply}")
    if total > 0:
        conversation.append(f"💰 **Current total:** ${total}")

    # --- Update chat area ---
    chat_area.object = "\n\n".join(conversation)
    user_input.value = ""  # clear input

# Bind button
send_button.on_click(handle_order)

# --- Layout ---
dashboard = pn.Column(
    "# 🍔 Foodie Chatbot",
    user_input,
    send_button,
    chat_area,
    sizing_mode="stretch_width"
)

dashboard.servable()
