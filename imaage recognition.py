import cv2
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import json
import datetime

# Load the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Descriptions (add more as needed)
descriptions = [
    "a red cup", "a blue cup", "a chair", "a cat", "a dog", "a laptop",
    "a plant", "a book", "a car", "a phone", "a bicycle", "a bottle",
    "a pair of shoes", "a keyboard", "a street art painting"
]

def identify_and_save_object(frame, output_data):
    # Convert the frame to a PIL Image
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    # Encode the image and descriptions
    inputs = processor(
        text=descriptions, images=image, return_tensors="pt", padding=True
    )
    
    # Get model outputs
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)  # Convert to probabilities
    
    # Find the highest probability description
    max_prob_index = probs.argmax().item()
    identified_description = descriptions[max_prob_index]
    confidence = probs[0, max_prob_index].item()
    
    # Save data
    data_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "description": identified_description,
        "confidence": confidence
    }
    output_data.append(data_entry)
    
    # Print the description
    print(f"Identified: {identified_description} with confidence {confidence:.2f}")
    
    return output_data

def main():
    # Initialize camera
    cap = cv2.VideoCapture(0)
    
    # Storage for results
    output_data = []
    
    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                break
            
            # Identify object in the frame
            output_data = identify_and_save_object(frame, output_data)
            
            # Display the frame
            cv2.imshow("Camera", frame)
            
            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Save the recognized data to a JSON file
        with open("results.json", "w") as outfile:
            json.dump(output_data, outfile, indent=4)
            
    finally:
        # When everything is done, release the capture and close windows
        cap.release()
        cv2.destroyAllWindows()
        print("Data saved to results.json.")

# Run the script
if __name__ == "__main__":
    main()
