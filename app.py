import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Ensure input/output directories exist
chef_dir = os.path.join(os.path.dirname(__file__), 'chef')
ansible_dir = os.path.join(os.path.dirname(__file__), 'ansible')
os.makedirs(chef_dir, exist_ok=True)
os.makedirs(ansible_dir, exist_ok=True)

# Initialize Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Prompt engineering template
PROMPT_TEMPLATE = (
    "You are an expert in DevOps automation. Convert the following Chef recipe into an equivalent Ansible playbook. "
    "Preserve all logic, resources, and comments. Output only a valid Ansible YAML playbook.\n\nChef Recipe:\n{chef_code}\n\nAnsible Playbook:"
)

def convert_chef_to_ansible(chef_code):
    prompt = PROMPT_TEMPLATE.format(chef_code=chef_code)
    response = genai.GenerativeModel("gemini-2.5-flash").generate_content(prompt)
    return response.text.strip()

# Process all Chef recipes in the chef directory
for filename in os.listdir(chef_dir):
    chef_path = os.path.join(chef_dir, filename)
    if os.path.isfile(chef_path):
        with open(chef_path, 'r', encoding='utf-8') as f:
            chef_code = f.read()
        ansible_playbook = convert_chef_to_ansible(chef_code)
        ansible_path = os.path.join(ansible_dir, os.path.splitext(filename)[0] + '.yml')
        with open(ansible_path, 'w', encoding='utf-8') as f:
            f.write(ansible_playbook)
        print(f"Converted {filename} to {os.path.basename(ansible_path)}")
