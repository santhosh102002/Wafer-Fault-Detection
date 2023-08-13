from flask import Flask, render_template, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os,sys

from src.pipelines.training_pipeline import TrainPipeline

from src.pipelines.prediction_pipeline import PredictionPipeline



app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome </h1>"

@app.route('/train')
def train_route():
    try:
        train_pipeline = TrainPipeline()
        run_pipeline = train_pipeline.run_pipeline()
        return "<h1>Training Completed</h1>"
    except Exception as e:
        raise CustomException(e,sys)
@app.route('/upload',methods = ['POST','GET'])
def upload_data():
    try:
        if request.method == 'POST':
            prediction_pipeline = PredictionPipeline(request)
            prediction_file_detail = prediction_pipeline.run_pipeline()

            lg.info("prediction completed. Downloading prediction file.")
            return send_file(prediction_file_detail.prediction_file_path,
                            download_name= prediction_file_detail.prediction_file_name,
                            as_attachment= True)


        else:
            return render_template('upload_file.html')
    except Exception as e:
        raise CustomException(e,sys)


if __name__ == "__main__":

    app.run()