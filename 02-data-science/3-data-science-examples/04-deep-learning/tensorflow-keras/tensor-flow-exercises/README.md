Exercises
===========================================================

Building the Docker container
-----------------------------

    docker build -t $USER/exercises .

Running the container
---------------------

    docker run -p 8888:8888 -it --rm $USER/exercises

## What Comes Next

This README is only for running the exercise container.

1. Return to the parent TensorFlow or Keras tutorial folder for the actual learning sequence.
2. Use this container only when you specifically want the exercise environment, not as your entry point into the deep-learning section.
