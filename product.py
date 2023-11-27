# SETUP INSTRUCTIONS:
# 1. Install openai with pip install --upgrade openai
# 2. Create an API key on the OpenAI website
# 3. Add the following to ~/.bashrc or ~/.zshrc: export OPENAI_API_KEY='your-key-here'

# Initialize OpenAI client instance
from openai import OpenAI
client = OpenAI()

############## EXAMPLE ######################

# Generate a chat completion from ChatGPT
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a university student with lots of homework to do this week."},
    {"role": "user", "content": "How should I study for my machine learning quiz that is in 3 days?"}
  ]
)

# Get generated message in readable form
gen_text = completion.choices[0].message.content
gen_text_newline = gen_text.replace('\\n', '\n')

# Print
print(completion)
print("============================")
print("Generated Text:")
print("============================")
print(gen_text_newline)

############## END EXAMPLE ##################

############## PROJECT ######################

