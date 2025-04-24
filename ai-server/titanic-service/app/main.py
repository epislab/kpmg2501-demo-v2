import os
import sys

# Add the project root directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from app.domain.controller.titanic_controller import TitanicController

def main():
    # Create TitanicController instance
    controller = TitanicController()
    
    # Define file paths
    train_fname = 'train.csv'
    test_fname = 'test.csv'
    
    # Execute preprocessing
    print("Starting preprocessing...")
    processed_data = controller.preprocess(train_fname, test_fname)
    print("Preprocessing completed successfully!")
    
    # Execute learning
    print("Starting learning...")
    controller.learning()
    
    # Execute evaluation
    print("Starting evaluation...")
    controller.evaluation()
    
    # Execute submission
    print("Starting submission...")
    controller.submit()

if __name__ == "__main__":
    main()
