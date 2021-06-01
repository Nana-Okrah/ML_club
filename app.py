from flask import Flask, render_template, request, current_app as app
from pycoral.utils.dataset import read_label_file
import vision

app = Flask(__name__)

@app.route('/')
def working():
	classifier = vision.Classifier(vision.CLASSIFICATION_MODEL)
	# Run a loop to get images and process them in real-time
	for frame in vision.get_frames():
		classes = classifier.get_classes(frame)
		# Get list of all recognized objects in the frame
		label_id = classes[0].id# list of id
		score = classes[0].score# condidence score 
		labels = read_label_file(vision.CLASSIFICATION_LABELS)
		label = labels.get(label_id)# getting the labels id
		print(label, score)
		return render_template(index.html,label=label,score=score)
#if score < =float(0.60):
	print(label,score,link)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
