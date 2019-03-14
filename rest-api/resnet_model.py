from io import BytesIO
from fastai.vision import load_learner, open_image

class MyResnetModel(object):
    def __init__(self, weights_path):
        try:
            self.learn = load_learner(weights_path, fname='weights.pkl')
        except RuntimeError as e:
            if len(e.args) > 0 and 'CPU-only machine' in e.args[0]:
                print(e)
                message = "\n\nThis model was trained with an old version of fastai and will not work in a CPU environment.\n\nPlease update the fastai library in your training environment and export your model again.\n\nSee instructions for 'Returning to work' at https://course.fast.ai."
                raise RuntimeError(message)
            else:
                raise
        print("Successfully loaded model")

    def predict(self, img_bytes):
        img = open_image(BytesIO(img_bytes))
        prediction = self.learn.predict(img)[0]

        return str(prediction)

