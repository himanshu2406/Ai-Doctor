# Ai-Doctor

![GitHub contributors](https://img.shields.io/github/contributors-anon/himanshu2406/Ai-Doctor?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/himanshu2406/Ai-Doctor?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/himanshu2406/Ai-Doctor?style=for-the-badge)
![GitHub closed issues](https://img.shields.io/github/issues-closed/himanshu2406/Ai-Doctor?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/himanshu2406/Ai-Doctor?style=for-the-badge)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/himanshu2406/Ai-Doctor?style=for-the-badge)
![Github Total lines](https://tokei.rs/b1/github/himanshu2406/Ai-Doctor)

| Information | Discord | Donate |
|:------------|:---------|:-------|
| Open source discord bot for Ai pneumonia detection, Detects diseases within seconds with just an xray scan <br><br> We are constantly adding new features to the discord bot, this project is maintained by Anondoser but it has been made Open Source so that everyone can contribute ! | [![Discord server](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.icons8.com%2Fcolor%2F2x%2Fdiscord-logo.png&f=1&nofb=1)](https://discord.gg/ZUGVPSS) | [![BuyMeACoffee](https://www.buymeacoffee.com/assets/img/guidelines/logo-mark-1.svg)](https://www.buymeacoffee.com/anondoser/shop) |

**Join** our Discord bot now ! [here](https://discord.gg/ZUGVPSS)
**Blog** is out , Read more [here](https://anondoser.xyz/2020-07-07-How-i-made-an-Ai-Doctor/) !
#### IMPORTANT : This is a test software not meant for real life applications , it's always recommended to consult a real doctor !

# Features:

1. Now you can add the bot in your own server ! - [here](https://discord.com/api/oauth2/authorize?client_id=729677023877791805&permissions=645121&scope=bot)
2. Detects whether a person has pneumonia or not based on a chest X-ray ; Has an accuracy of 98+ .
3. Trained on a dataset of 2.29 Gb (https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
4. Model Used - CNN (Convolutional neural network)
5. Accuracy - 98% + ! (steps =500, epochs = 10, val_steps = 125 )
6. trained model size = 9 Mb so you don't have to worry about downloading the entire 2.29Gb to test the model


# HOW TO PREDICT ON NEW IMAGES :

1. go to https://discord.gg/ZUGVPSS and pass in the comand !d along with your image url and get back the result within seconds ! 

### Alternative : 

1. go to https://colab.research.google.com/
2. press upload and upload the .h5 file (pneumonia_pred_new.h5)
3. press upload and upload the x-ray image you want to run the prediction on.

4. Then paste the following code in the notebook cell:
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
