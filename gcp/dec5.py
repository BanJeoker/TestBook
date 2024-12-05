from vertexai.preview.language_models import ChatModel

# Define the simulated weather function
def get_weather(location):
    weather_data = {
        "New York": {"temperature": "15°C", "condition": "Cloudy"},
        "San Francisco": {"temperature": "20°C", "condition": "Sunny"},
    }
    return weather_data.get(location, {"temperature": "Unknown", "condition": "Unknown"})

# Define the function schema
function_definition = {
    "name": "get_weather",
    "description": "Fetches the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The name of the location."},
        },
        "required": ["location"],
    },
}

# Initialize GeminiPro model
chat_model = ChatModel.from_pretrained("chat-gpt-pro")  # GeminiPro

# Create a chat session
chat = chat_model.start_chat()

# User query
query = "What is the current temperature in New York?"

# Call the model with function definitions
response = chat.send_message(
    query,
    functions=[function_definition],  # Add function definitions
    temperature=0.0,
)

# Process the response
if response.function_call:
    # If the model suggests a function call
    suggested_function = response.function_call
    if suggested_function["name"] == "get_weather":
        location = suggested_function["parameters"]["location"]
        # Call the function with suggested parameters
        weather_info = get_weather(location)
        # Generate final response using the function output
        final_response = (
            f"The current temperature in {location} is {weather_info['temperature']} "
            f"and the weather is {weather_info['condition']}."
        )
    else:
        final_response = "The model requested an unsupported function."
else:
    # If no function call was suggested
    final_response = response.text

# Print the final response
print(final_response)
