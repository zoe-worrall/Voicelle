
# this is what makes the conversion possible - we may need to have the user
#   install ffmpeg
import ffmpeg

# this is a place holder for when we are able to upload videos into the application
name = input('Name of File: ')

# takes in the file that the user input; the file, currently, needs to be in the same folder as the code
stream = ffmpeg.input(name)
# separates the audio from the video file
audio = stream.audio
# creates a new ouput called 'outAudioWebM.wav' with the audio file that was created
out = ffmpeg.output(audio, 'outAudioWebM.wav')
# runs/(maybe opens, if you are on Windows) the file, just to listen to it and make sure it works
out.run()
