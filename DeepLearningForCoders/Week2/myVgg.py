
from keras.preprocessing import image



class Vgg16():
    """The VGG 16 Imagenet model"""

    def __init__(self):
        
        
    def get_batches(self, path, gen=image.ImageDataGenerator(), shuffle=True, batch_size=8, class_mode='categorical'):
        return gen.flow_from_directory(path, target_size=(224,224),
                                      class_mode=class_mode, shuffle=shuffle, batch_size=batch_size)
        