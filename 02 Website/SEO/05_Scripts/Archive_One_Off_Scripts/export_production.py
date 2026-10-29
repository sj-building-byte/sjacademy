filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/resources_vault.html"
prod_filepath = "/Users/sunyyanjunaid/Documents/WEbsite SEO/resources_vault_elementor.html"

with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Extract just the style, widget root, and script
import re

style_match = re.search(r'<style>.*?</style>', html, re.DOTALL)
widget_match = re.search(r'<div id="sja-widget-root">.*?</div>\n\n<script', html, re.DOTALL)
script_match = re.search(r'<script type="module">.*?</script>', html, re.DOTALL)

if style_match and widget_match and script_match:
    # Need to remove the "\n\n<script" part from the end of widget_match
    widget_html = widget_match.group(0).replace('\n\n<script', '')
    
    # We also want to include the Google Fonts import at the top of the style
    fonts = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">\n'
    
    prod_html = fonts + style_match.group(0) + "\n\n" + widget_html + "\n\n" + script_match.group(0)
    
    with open(prod_filepath, "w", encoding="utf-8") as f:
        f.write(prod_html)
    print("Production file created!")
else:
    print("Error extracting parts.")
