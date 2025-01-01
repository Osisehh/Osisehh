import re

# Define the animation styles
animation_styles = """
<style>
@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@keyframes slideIn {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(0); }
}

.fadeIn {
  animation: fadeIn 2s ease-in-out infinite;
}

.slideIn {
  animation: slideIn 3s ease-in-out infinite;
}
</style>
"""

# Read the README file
with open("README.md", "r") as file:
    readme_content = file.read()

# Insert the animation styles into the README content
updated_readme_content = re.sub(
    r"<!-- Start of the animated section -->",
    f"<!-- Start of the animated section -->\n{animation_styles}",
    readme_content
)

# Write the updated content back to the README file
with open("README.md", "w") as file:
    file.write(updated_readme_content)
