## Local env

To run this application you need to have installed pyenv and docker

```
brew install pyenv
```

[Docker Installation Guide](https://docs.docker.com/engine/install/)

You will also need to create a .env file in root to have the password for encryption

```
ENCRYPT_PWD=<your_password>
```

To setup your local env you can run

```
make build-env
```

(To setup and run the app)

```
make setup
```

To deploy using minikube, must run

`eval $(minikube docker-env)`

And then build the image using

`docker build --no-cache -t simple_app .`

### Application

simple API app  receives the following request:

```json
{ "payload": "do_the_thing" }
```

where do_the_thing is arbitrary string
and respond with status 200 and data:

```json
{
  "thing": {
    "current_time": "2022-12-10T13:49:51.141Z",
    "encrypted_payload": "U2FsdGVkX1/wYkqq7xFYRiA7Q9hylAT+",
    "emoji": ":smile:"
  }
}
```

both request and response should be encoded in json

response contains:

- `current_time` - string formatted current time on the server at the time of serving request
- `encrypted_payload` - string which was received in payload on request encrypted with des-ede-cbc cypher and pre-defined password
- `emoji` - random emoji :shortcode: from the [repo][2]


## Deploying the Application on Minikube

To deploy the application to a local Minikube cluster, follow these steps:

1. **Start Minikube**
    ```
    minikube start
    ```

2. **Enable the Ingress Controller Addon**
    ```
    minikube addons enable ingress
    ```

3. **Build and Tag Docker Image (Ensure you are at the root of your application directory)**

    ```
    eval $(minikube docker-env)
    docker build -t simple_app .
    ```
4. **Deploy the Application**

    ```
    kubectl apply -f k8s
    ```

5. **Update Hosts File**

    This maps the `simple-app.local` domain to your Minikube IP.
    ```
    sudo echo "127.0.0.1 simple-app.local" | sudo tee -a /etc/hosts
    ```

6. **Execute minikube tunnel**

    An intermediary step to enable ingress
    ```
    minikube tunnel
    ```

Now, you can access the application via: https://simple-app.local

**Note:** You will see a security warning in your browser as it does not trust the self-signed certificate. You can proceed for testing purposes

[1]: https://12factor.net/
[2]: https://github.com/iamcal/emoji-data 