# Introdution

## Tasks

- [x] Install python
- [ ] Install google app engine

## On Mac
The instruction in the video is quite old, and it doesn't work anymore. Follow new instruction below

Follow [this](https://drive.google.com/file/d/0Byu3UemwRffDc21qd3duLW9LMm8/view) for full instruction in all OS

#### Step 1: Create a project on Google App Engine
Follow this [guide](https://console.cloud.google.com/start) to create a project on Google App Engine

#### Step 2: Install `gcloud`
Follow this [instruction](https://cloud.google.com/sdk/docs/#linux) which is provided by Google.

#### Step 3: Install `app-egine-python`
```
gcloud compoments install app-egine-python
```

#### Step 4: Clone `python-doc-samples` from Github
```
git clone https://github.com/GoogleCloudPlatform/python-docs-samples
```

#### Step 5: Run `hello world web app` locally
```
dev_appserver.py /path/to/hello-world
```
Now, goto `127.0.0.1:8080` to see !

#### Step 6: Deploy your project to cloud (google cloud)
```
gcloud app deploy
```

## Notes
- To learn more how Google cloud work, check this [guide](https://cloud.google.com/appengine/docs/standard/python/quickstart#hello_world_code_review)





