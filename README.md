
<h1 align="center">
tts_dataset_recorder
</h1>
this is a work in progress python project used to make datasets for voice cloning. <br><br>
hopefully when it is done, it will make the processs of makeing a datasets easier. **not offline**


<h2 align="center">
Basic Idea
</h2>  

records audio in .wav format <br>
converts audio text using speech recognition <br>
outputs to csv<br>
each recording is **10** seconds long and will begin after the countdown. Any any more than 10 seconds might break because it is using google's text to speech<br>
<br>
<br>


<h3 align = "center" >
installation and setup
</h3>

you can use the executable file to run and install the recorder, the installer can be found [--> here <--](https://github.com/clayton14/tts_dataset_recorder/releases) <br>
  
<h3>
run with python
</h3>

create a python virtual environment by running the following command in the working directory
>python -m venv .
>python -m pip install -r requirements.txt

if you get an error with py audio you might have to install the .whl manually using. <br>
>pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl

The one in this repo is the one that worked for me, if you are having troubble go [here](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14) for reference.

**To start the program run**
>python record.py 
