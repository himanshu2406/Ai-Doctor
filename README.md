# Ai-Doctor

Open source discord bot for ai pneumonia detection.
Detects diseases within seconds with just an xray scan

# IMPORTANT : This is a test software not meant for real life applications , it's always recommended to consult a real doctor !

Discord server with ready to use Ai Doctor : https://discord.gg/ZUGVPSS

Now you can add the bot in your own server ! - 
https://discord.com/api/oauth2/authorize?client_id=729677023877791805&permissions=645121&scope=bot


Detects whether a person has pneumonia or not based on a chest X-ray ; Has an accuracy of 98+ .

Trained on a dataset of 2.29 Gb (https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

Model Used - CNN (Convolutional neural network)
Accuracy - 98% + ! (steps =500, epochs = 10, val_steps = 125 )

trained model size = 9 Mb so you don't have to worry about downloading the entire 2.29Gb to test the model


# HOW TO PREDICT ON NEW IMAGES :

go to https://discord.gg/ZUGVPSS and pass in the comand !d along with your image url and get back the result within seconds ! 

Alternative : 

go to https://colab.research.google.com/
press upload and upload the .h5 file (pneumonia_pred_new.h5)
press upload and upload the x-ray image you want to run the prediction on.

Then paste the following code in the notebook cell:
(Remember to replace the your_image.jpeg with the real name of the image)
Now run the code and see the prediction with accuracy after scrolling down !

CODE:-
https://pastebin.com/srVfAYLD

### Acknowledgements

Data: https://data.mendeley.com/datasets/rscbjbr9sj/2

License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

Citation: http://www.cell.com/cell/fulltext/S0092-8674(18)30154-5

## Discord - Firelogger#7717
### Reddit - https://www.reddit.com/r/discordapp/comments/hmasi2/i_made_a_discord_bot_that_detects_diseases_using/
