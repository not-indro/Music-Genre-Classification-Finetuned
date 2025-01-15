import os
from fastapi import FastAPI, File, UploadFile
from transformers import AutoFeatureExtractor, AutoModelForAudioClassification
import torch
import soundfile as sf

app = FastAPI()

# Load the fine-tuned model and feature extractor
feature_extractor = AutoFeatureExtractor.from_pretrained("itsindro/distilhubert-finetuned-gtzan")
model = AutoModelForAudioClassification.from_pretrained("itsindro/distilhubert-finetuned-gtzan")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read the uploaded audio file
    audio, sr = sf.read(file.file)
    # Preprocess the audio
    inputs = feature_extractor(
        audio,
        sampling_rate=sr,
        return_attention_mask=True,
        padding="max_length",
        max_length=16000 * 30,  # 30 seconds
        truncation=True,
        return_tensors="pt"
    )
    # Run inference
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class = torch.argmax(logits, dim=-1).item()
    # Get the label name
    label = model.config.id2label[predicted_class]
    return {"predicted_genre": label}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))  # Use PORT environment variable or default to 8080
    uvicorn.run(app, host="0.0.0.0", port=port)