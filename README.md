# Installation
If Windows, install visual studio code build tools >= 2015 and restart.

`pip install rasa`


# Train model
`rasa train [--augmentation 20]`


# Chat

## Run action server
`python -m rasa_sdk --actions actions`

## Start chat (in another terminal)
`rasa shell [--debug]`

Use `rasa shell nlu` for NLU debugging


# Run tests

`rasa test [--fail-on-prediction-errors]`


# Emojis Attribution
All emojis designed by [OpenMoji](https://openmoji.org/) – the open-source emoji and icon project. License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/#)
