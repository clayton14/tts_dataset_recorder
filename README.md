
<h1 align="center">
tts_dataset_recorder
</h1>
this is a work in progress python project used to make datasets for voice cloning. <br><br>
hopefully when it is done, it will make the processs of makeing a datasets easier. **not offline**


<h2 align="center">
Basic Idea
</h2>  

records audio in .wav format <br>
converts to text using speech recognition <br>
outputs to csv<br>
each recording is **10** seconds long and will begin after the countdown. Any any more than 10 seconds might break because it is using google's text to speech<br>
<br>
<br>


<h2 align = "center" >
installation and setup
</h2>

<h3>
run 
</h3>

> python -m pip install -r requirements.txt

if you get an error with py audio you might have to install the .whl manually. <br>
The one in this repo is the one that worked for me, if you are having troubble go [here](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14) for reference.

**To start the program run**
>python record.py 
