from flask import Flask, send_file

app = Flask(__name__)

@app.route('/<int:image_number>')
def serve_image(image_number):
    image_path = f'gs://task2a-bucket/image{image_number}.jpg'
    caption = f'Caption for Image {image_number}'
    # HTML 
    html_response = f'<h1>{caption}</h1><img src="{image_path}">'
    return html_response

if __name__ == '__main__':
    app.run(debug=True)