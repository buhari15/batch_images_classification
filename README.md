# From model to production

Simple images classification model using the Keras Sequential API.

The classification is run on batch at midmight. 

Jenkins pipeline is used to schedule a batch prediction with a Flask API endpoints.
Graphical representation of the processes. <br>
![Process](https://github.com/buhari15/batch_images_classification/blob/master/process.png)

If new images are found on the images folder, the model will predict the classes of the new found images. 

The classification result is save in csv file and push to Github. Below is the output of the classification.
* The output of batch classification of images.<br>
![Output for batch result](https://github.com/buhari15/batch_images_classification/blob/master/Screenshot%202023-05-19%20at%2016.46.05.png)

If the model can not find new images, it will not save any result.<br>
* The output of batch classification if no new images are found in Jenkins.
![No new images are found](https://github.com/buhari15/batch_images_classification/blob/master/No_new_images.png)

Basic model metrics can be found below:
![Metrics](https://github.com/buhari15/batch_images_classification/blob/master/code/metrics.py)

It also possible to load images from the AWS S3. While the result can be save into MongoDB.<br>
Check here for the code ![config](https://github.com/buhari15/batch_images_classification/blob/master/code/metrics.py)


## Author

**Buhari Abubakar**

+ [github/buhari15](https://github.com/buhari15)

## License

Copyright © 2023 Buhari Abubakar
Released under the MIT license.

***
