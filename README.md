# 💥 Minesweeper-Py
![Home Screen](https://github.com/daverencordero/Minesweeper-Py/blob/main/README/minesweeper-py-01.png?raw=true)

#### About

For our final project in the course subject *"CMSC 12: Introduction to Programming"*, we were tasked to create a game using python. At first it was a dawning task since I was under the assumption that we were not allowed to use OOP since it has not been taught yet (I'm already very proficient with it). However, the rule was later redacted and I ended up having to finish this output in **less than a week**. If you would look at the code, you would realize that I didn't utilize the pygame library effectively due to my scarcity of time in learning it and thus I only utilized its sprite capabilities and made all of the game's logic in custom which I'm already familiar off due to my previous exposure to game development. I'm very happy over how it turned out although I believe I could've made better assets for it if granted enough time.

#### Features

<u>Home Screen with High Score Viewer</u>

For the features, nothing out of the ordinary. Of course, there's a home screen scene where there is the caption, play button and the high score button. 

![High Score Screen](https://github.com/daverencordero/Minesweeper-Py/blob/main/README/minesweeper-py-02.png?raw=true)

I was actually having a lot of trouble with typing in this particular scene because of the dynamic typing in Python. Also, it took me longer than expected because I haven't got exposed to web development at the time and wasn't that knowledgeable over modern programming practices. 



<u>Game mode Selection Screen</u>

![Game mode Selection Screen](https://github.com/daverencordero/Minesweeper-Py/blob/main/README/minesweeper-py-04.png?raw=true)

There's also a game mode selection screen with a load game feature. It's pretty simple, selecting the certain game modes just edits the size of the mine field in game proper. The load game feature simply loaded the game state from a text file using a pseudo csv format to represent the in game cell matrix. There's a save button in the game screen that brings functionality to this feature.



<u>Game Screen</u>

![Game Screen](https://github.com/daverencordero/Minesweeper-Py/blob/main/README/minesweeper-py-03.png?raw=true)

The game screen is pretty simple. It presents the minefield, a timer, a home button, and a save button as introduced earlier. The logic behind this is pretty lackluster and inefficient. All the images are pre-rendered and that's why the screen lags behind when creating a large mine field. I think I could've designed this better but I supposed it is still somehow serviceable.



#### Regrets?

I believe I could've provided better assets for the game especially since not only is the color scheme really good, I also developed a very flexible sprite loading system. In addition, I spent a lot of my time doing relative position logic so that the game is playable at any window size (Talk about *responsive* design). It's quite unfortunate that I wasn't able to showcase it in the final product properly. Also, I didn't get to do the logic that would save and continue the in game timer. Good thing my professor didn't catch that bug (Or did she?). That pretty much sums up my regrets. I still like the final product and will perhaps attempt to better it one day. 