# 5.10 Homework

## Question 1

Version of Pipenv: **2021.5.29**

## Question 2

Checksum for Scikit-Learn 1.0:

```
sha256=edc3ae8b6149cf68043e309c942c6df1b24800ee80835c4473379da2323cf861
```

## Question 3

Probability of churning (Script): **0.115**

Commands:

```
docker build -t homework05 .

docker run -it --rm -p 9696:9696 homework05:latest
```

Customer to score:

```json
{"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}
```

## Question 4

Probability of churning (Flask): **0.998**

Customer to score:

```json
{"contract": "two_year", "tenure": 1, "monthlycharges": 10}
```

## Question 5

Digest for the base image (Docker):

```
sha256:1ee036b365452f8a1da0dbc3bf5e7dd0557cfd33f0e56b28054d1dbb9c85
```

Commands:

```
docker build -f Dockerfile-agrigorev -t homework05-question5:latest .

docker run -it --rm  -p 9696:9696 homework05-question5:latest
```

## Question 6

Probability of churning (Docker): **0.329**

```json
{"contract": "two_year", "tenure": 12, "monthlycharges": 10}
```
