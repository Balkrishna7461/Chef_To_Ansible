# Chef_To_Ansible
This app automatically converts Chef recipes into equivalent Ansible playbooks using Google Gemini 2.5 Flash. Place your Chef .rb files in the chef folder, and the app will generate corresponding Ansible .yml playbooks in the ansible folder, preserving all logic, resources, and comments.

## Requirements
- Python 3.8+
- See `requirements.txt` for Python dependencies

## Setup & Usage

1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd chef_to_ansible
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your Gemini API key**
   - Create a `.env` file in the `chef_to_ansible` directory with the following content:
     ```env
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

5. **Add Chef recipes**
   - Place your `.rb` Chef recipe files in the `chef` folder.

6. **Run the app**
   ```sh
   python app.py
   ```
   - Converted Ansible playbooks will appear in the `ansible` folder.

## Example
- Input: `chef/install_apache.rb`
- Output: `ansible/install_apache.yml`

## Notes
- Ensure your Gemini API key is valid and has access to the Gemini 2.5 Flash model.
- The app uses prompt engineering to maximize conversion quality.
