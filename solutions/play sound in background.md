## SOLUTION: Playing sound in the background

***SCENARIO:*** You want two things to happen; your code running as normal WHILE sound plays in the background throughout!

## IMPORTANT NOTE: Your Alta3 BCHD machine does not support sound or graphics. To use this, you'll need to run it on your personal machine.

```python
import winsound

winsound.PlaySound("/path/to/a/sound/file/you/want/to/play.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS )

print("Sound should now be playing and look! You're typing in an input while doing so!")
print("Your code will continue to run while music plays, and music will stop when the code stops.")
input("Press ENTER to stop the song.")

winsound.PlaySound(None, winsound.SND_ASYNC)
```
