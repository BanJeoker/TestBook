from vertexai.language.models import TextGenerationModel

# Simulate a weather function (replace this with an actual API call)
def get_weather(location):
    weather_data = {
        "New York": {"temperature": "15°C", "condition": "Cloudy"},
        "San Francisco": {"temperature": "20°C", "condition": "Sunny"},
    }
    return weather_data.get(location, {"temperature": "Unknown", "condition": "Unknown"})

# Define the ReAct function structure
function_definition = {
    "name": "get_weather",
    "description": "Fetches the current weather for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {"type": "string", "description": "The name of the location."}
        },
        "required": ["location"],
    },
}

# Initialize the model
model = TextGenerationModel.from_pretrained("text-bison")

# User query
query = "What is the current temperature in New York?"

# Call the model with function definitions
response = model.predict(
    query,
    temperature=0.0,
    candidate_count=1,
    functions=[function_definition],
)

# Model's suggestion
if response.function_call:
    suggested_function = response.function_call
    if suggested_function["name"] == "get_weather":
        location = suggested_function["parameters"]["location"]
        # Call the function with the suggested parameters
        weather_info = get_weather(location)
        
        # Generate a final response using the function's output
        final_response = (
            f"The current temperature in {location} is {weather_info['temperature']} "
            f"and the weather is {weather_info['condition']}."
        )
    else:
        final_response = "The model requested an unsupported function."
else:
    # If no function call was suggested, use the generated response
    final_response = response.text

print(final_response)
