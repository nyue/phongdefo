import hou
import os
from jinja2 import Template

# Where am I?
this_path = os.path.dirname(os.path.realpath(__file__))

template_file = os.path.join(this_path, "phongdefo.json.in")
# Load the template from a file
with open(template_file, "r") as file:
    template_content = file.read()

# Create a Jinja2 Template object
template = Template(template_content)

# Get the Houdini user preference directory
user_pref_dir = hou.getenv("HOUDINI_USER_PREF_DIR")
#print("User Preference Directory:", user_pref_dir)

# Get user-provided values
user_data = {
    "houdini_path": this_path
}

# Render the template with the user's data
result = template.render(user_data)

phongdefo_json_path = os.path.join(user_pref_dir, "packages", "phongdefo.json")
# Save the result to a new file or display it
with open(phongdefo_json_path, "w") as output_file:
    output_file.write(result)

#print(f"Template rendered and saved to {phongdefo_json_path}.")
