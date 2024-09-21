import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

def preprocess_images(input_dir, output_dir):
    """
    Preprocess CIFAR-10 images using TensorFlow's ImageDataGenerator.
    """
    datagen = ImageDataGenerator(rescale=1.0/255.0)

    for img_name in os.listdir(input_dir):
        img_path = os.path.join(input_dir, img_name)
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(32, 32))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = img_array.reshape((1,) + img_array.shape)

        for batch in datagen.flow(img_array, batch_size=1, save_to_dir=output_dir, save_prefix='aug', save_format='png'):
            break

if __name__ == "__main__":
    preprocess_images('data/raw/train', 'data/processed/')
