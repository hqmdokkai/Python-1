from flask import Flask
from flask import Flask, url_for
from markupsafe import Markup
import markdown
from flask import render_template
app = Flask(__name__)
def home():
    # Markdown content
    content = """
# IT!

Python free!

Video python below \/

<img src="/static/OIP.jpg" width="100%" height="100%" alt="Image description">

<div class="video">
    <iframe
        width="1280"
        height="720"
        src="https://www.youtube.com/embed/dam0GPOAvVI"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen
    ></iframe>
</div>

<h5>Thank you</h5>

<script>
    console.log("This developer tool is very dangerous. Don't enter the codes that strangers and relatives tell you to enter on the console or your device will be hacked.")
</script>
"""
    # Convert Markdown content to HTML
    html_content = markdown.markdown(content)

    # Render the HTML using a separate template file
    return render_template('index.html', html_content=html_content)

if __name__ == '__main__':
    app.run(debug=True)