# From model to production

In this project a simple images classification model was built using the Keras Sequential API.

The classification is run on batch at midmight. 

The Jenkins is used to schedule a batch prediction with a Flask API endpoints.
If new images are found on the images folder, the model will predict the classes of the new found images. 

The classification result is save in csv file and push to Github. Below is the output of the classification.
* The output of batch classification of images.<br>
![Output for batch result](https://github.com/buhari15/batch_images_classification/blob/master/Screenshot%202023-05-19%20at%2016.46.05.png)

If the model can not find new images, it will not save any result.<br>
* The output of batch classification if no new images are found.
![No new images are found](https://github.com/buhari15/batch_images_classification/blob/master/No_new_images.png)

## Author

**Buhari Abubakar**

+ [github/buhari15](https://github.com/buhari15)

## License

Copyright © 2023 Buhari Abubakar
Released under the MIT license.

***
