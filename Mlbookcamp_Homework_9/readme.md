# 9 Homework

## Question 1

The size of converted model is **43 MB**

## Question 2

The output index for this model is **13**

## Question 3

The value in the first pixel, the R channel, is **0.7058824**

## Question 4

Prediction of the model: **0.7704911**

## Question 5

The id of Docker image is **beedf6c73d95**

## Question 6

Commands:

```
docker build -t homework09 .

docker run -it --rm -p 8080:8080 homework09:latest
```

Prediction:

```json
{"dogs": 0.5413472652435303}
```

Prediction from Lambda in Docker container: **0.54**
