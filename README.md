# AI Cyberpunk Themed Story Writer

This project is an AI-powered story generator with a focus on Cyberpunk and futuristic themes. The program provides auto-complete suggestions and next word predictions based on the user's input. Additionally, users can undo their last input, creating an interactive and flexible story-writing experience.

## User Manual

### How to Use the Program

1. **Running the Program**:
   - To run the program, simply execute the `story_writer_app.py` file in a terminal:
     ```
     python3 story_writer_app.py
     ```

2. **Interacting with the Program**:
   - **Entering text**: You can type a part of the story, and the program will provide auto-complete suggestions for the current word and predict the next word.
   - **Auto-complete suggestions**: When you type a partial word, the program will suggest up to 5 possible completions. You can choose a number between 1 and the number of available suggestions or type your own word.
   - **Next word prediction**: After you input a word, the program will predict the next word or phrase, providing up to 5 suggestions. You can choose a number between 1 and the number of predictions or enter your own word.
   - **Undo last word**: If you made a mistake or want to remove the last word, type `undo` to delete the previous input.
   - **Exit the program**: When you are done writing, type `exit` to finish and display the full story.

## Interaction Record

The following example demonstrates how a user interacts with the AI Cyberpunk Themed Story Writer.

1. **User Input**: The user starts typing a part of the story:
![160561728826941_ pic](https://github.com/user-attachments/assets/e9424067-6d6e-42d8-b6b9-a72728fd0c36)

2. **Auto-complete Suggestions**: The program offers several auto-complete options for the last word entered:
![160571728826941_ pic](https://github.com/user-attachments/assets/2520de8b-cc9c-4018-8cb8-a43b4c782850)

3. **User Selection**: The user selects option 2:<br>
Auto-complete: The robotic assistant

4. **Next Word Prediction**: The program predicts the next possible word based on the last word "robotic assistant":
![160581728826941_ pic](https://github.com/user-attachments/assets/9e896413-0844-4039-9f8b-b27f15c961ec)

5. **Undo Last Input**: If the user wants to undo the last word, they can type `undo`:
![160621728828136_ pic](https://github.com/user-attachments/assets/3e476d7a-f1e6-4f7a-99fc-af1d9e1c4ff1)

6. **Exit**: When the user finishes writing, they can type `exit` to display the full story:
![160611728828136_ pic](https://github.com/user-attachments/assets/1498266f-20e8-47d3-812f-ab72997d46cc)
![160601728826941_ pic](https://github.com/user-attachments/assets/cb2d8a44-c8ef-4ac1-b2aa-f502e64d17e6)

This interaction record showcases how the user can input words, choose from auto-complete suggestions, predict the next word, and undo their last input in a seamless manner.

## Prediction Method

The `get_next_word_prediction` function is responsible for predicting the next word or phrase based on the user's input. It uses a predefined dictionary `word_pair_dict` that associates specific words with potential next words, particularly focusing on AI, robots, cyberpunk, and futuristic themes.

### Function Explanation

```python
def get_next_word_prediction(last_word, word_pair_dict):
    """Provides next word prediction based on the last word entered."""
    last_word = last_word.lower()  # Normalize the input to lower case
    if last_word in word_pair_dict:
        return word_pair_dict[last_word][:5]  # Return up to 5 predicted words or phrases
    return None

1. **Input**: The function takes the last word entered by the user and looks for it in the `word_pair_dict` dictionary.
   - The input word is first converted to lowercase to ensure that matching is case-insensitive.

2. **Dictionary Lookup**:
   - If the last word exists in the `word_pair_dict`, the function returns up to 5 potential next words or phrases. These next word predictions are predefined based on common associations in the cyberpunk and AI-themed domain.
   - For example, if the last word is `"robot"`, the function might return next word predictions such as `"revolution"`, `"assistant"`, `"control"`, `"worker"`, and `"intelligence"`.

3. **Return Value**:
   - If the word is found in the dictionary, the first 5 associated words or phrases are returned as suggestions.
   - If the word is not found in the dictionary, the function returns `None`, meaning no predictions are available.

### Example of `word_pair_dict`

The `word_pair_dict` is a dictionary that contains word pairs with up to 5 associated predictions. Here’s an example of how it is structured:

```python
word_pair_dict = {
    "robot": ["revolution", "assistant", "control", "worker", "intelligence"],
    "cybernetic": ["organism", "implant", "system", "enhancement", "body"],
    "artificial": ["intelligence", "life", "reality", "consciousness", "learning"],
    ...
}

When a user types a word like "robot", the function will search for this word in the word_pair_dict, and if found, it will provide the associated next words from the dictionary as predictions.
