# Text_generation_LSTM
This project demonstrates how to generate text using a Long Short-Term Memory (LSTM) neural network. The model is trained on the text of "The Master and Margarita" and uses Object-Oriented Programming (OOP) principles for structure and clarity.

## Features
- Text Generation: Generates text similar to "The Master and Margarita" after sufficient training.
- Modular Design: The project is organized into different modules for better maintainability.
- Customizable Training: Options to train from scratch or continue from a saved state.

## Technologies Used
- PyTorch: For building and training the neural network.
- NumPy: For numerical operations.
  
## Usage
To get started, clone the repository and install the required packages:

git clone <repository-url>
cd Text_generation_LSTM
pip install torch numpy
python main.py

There will be 3 options:
- Training: Select option 1 to start training the model. This may take several hours (4-5 hours for good results).
- Continue Training: If you want to continue training from a saved state, select option 3.
- Text Generation: You can implement a generator to create text based on the trained model (not shown in this snippet).

## Model Architecture
The model is an LSTM-based architecture with the following components:

- Embedding Layer: Converts input characters to dense vectors.
- LSTM Layer: Processes the sequences and captures long-term dependencies.
- Dropout Layer: Reduces overfitting by randomly setting some weights to zero during training.
- Fully Connected Layer: Maps LSTM outputs to character probabilities.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to create an issue or submit a pull request.
