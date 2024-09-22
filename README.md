# model-deployment  
This is a repo to get started with ML deployment. 
Steps to follow:  
1. create an environemnt using   
``pipenv install python==3.9 scikit-learn==1.5.2 flask``  
this will generate a Pipflie with the expected dependencies and packages.  
``pipenv lock`` generates the Pipfile.lock file.  
``pipenv shell`` or ``activate`` activates the environment  
``exit`` or ``deactivate`` deactivates it.  
2. After exporting your model for example with pickle  
``output_file = f'model_C=1.0.bin'``  
``with open(output_file, 'wb') as f_out:``  
``    pickle.dump((dv, model), f_out)``  
3. Create a python file (predict.py) that accepts html requests using Flask
Given an input a ML model will be used for inference.  
run ``python predict.py`` to serve the Flask application on the specifed port (test server use gunicorn for deployment)  
4. Create docker file defining instructions to create a docker image
    - python version
    - packages
    - define a working directory
    - files to copy in the docker image
    - install dependencies (use system python to istall dependencies)
    - Copy the model, the file to run and specify directory
    - define a port where app listens to incoming requests, set the port as open
    - define what to run when the docker image is built using entrypoint
    - build the docker image ``docker buid -t churn-service:v01 .``
    - run the docker image ``docker run -it --rm -p 9696:9696 churn-service:v01``
5. Cloud deploymnet in AWS using elastic Beanstalk  
    - install elastic beanstalk 
    - ``pip install awsebcli`` (preferablky with pipenv install)
    -  initalize project (type of the project -p flag)   
    ``eb init -p docker  churn-serving``
    - test locally  
    ``eb local run --port 9696``
    - creatie churn serving environemnt  
    ``eb create churn-serving-env``
    change the url used for serving and send request to the cloud.

Extra  
convert jupyter notebook to .py file with ``jupyter nbconvert --to=script predict.ipynb``