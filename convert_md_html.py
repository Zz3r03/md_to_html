import markdown
import sys

def convert_md_to_html(md_file, html_file):
    # Read the content of the Markdown file
    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    # Convert Markdown to HTML with fenced code blocks support
    html_content = markdown.markdown(md_content, extensions=['fenced_code'])
    
    # Write the HTML content to the output file
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

if __name__ == "__main__":
    # Specify the Markdown file to convert and the output HTML file
    if len(sys.argv) < 3:
        print("Usage: python convert_md_to_html.py <input_file.md> <output_file.html>")
    else:
        md_file = sys.argv[1]
        html_file = sys.argv[2]
        convert_md_to_html(md_file, html_file)
        print(f"Converted {md_file} to {html_file}")
