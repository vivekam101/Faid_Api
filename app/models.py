class ML_Model(object):
    def __init__(self):
        self.model_config = None
        self.model = None
        self.encoders = []
        
        self.test_accuracy = None