## Morning Exercise: Dictionary Modeling!

Follow the flowchart below to determine if you are, in fact, a horse.

!["Are You A Horse?" Flowchart](https://github.com/csfeeser/images/blob/master/12-Am-I-a-horse-flowchart.jpg?raw=true)

### Your Objective:

For brevity's sake, you've been provided a dictionary below that maps the flowchart above. Can you write a script using the dictionary `quiz` that prompts the user appropriately, mimicking the flow of the flowchart above?

```python
quiz= {
"1":{
    "question": "Aye you a horse?",
    "yes": "2",
    "no":"end"
    },
"2":{
    "question": "Do you walk on four legs?",
    "yes": "3",
    "no": "end"
    },
"3":{
    "question": "Really?",
    "yes": "4",
    "no": "end"
    },
"4":{
    "question": "Can you read and write?",
    "yes": "end",
    "no": "5"
    },
"5":{
    "question": "Liar, you're reading this.",
    "yes": "end",
    "no": "end"
    },
"end":{
    "question": "You're not a horse.",
    }
}
```
