# From model to production

In this project a simple images classification model was built using the Keras Sequential API.

The classification is run on batch at midmight. 

The Jenkins is used to schedule a batch prediction with a Flask API endpoints.
If new images are found on the images folder, the model will predict the classes of the new found images. 

The classification result is save in csv file and push to Github. Below is the output of the classification.
* The output of batch classification of images.
![First output from MongoDB](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/Screen_shoots/Reading_first_data.png](https://github.com/buhari15/batch_images_classification/blob/master/Screenshot%202023-05-19%20at%2016.46.05.png)

If the model can not find new images, it will not save any result. 
* The output of batch classification if no new images are found.
![First output from MongoDB](https://github.com/buhari15/Stream_Iot_to_MongoDB/blob/master/Screen_shoots/Reading_first_data.png](https://github.com/buhari15/batch_images_classification/blob/master/Screenshot%202023-05-19%20at%2016.46.05.png](https://github.com/buhari15/batch_images_classification/blob/master/No_new_images.png)

## Author

**Buhari Abubakar**

+ [github/buhari15](https://github.com/buhari15)

## License

Copyright © 2023 Buhari Abubakar
Released under the MIT license.

***
