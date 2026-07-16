import subprocess
import torch

def process_audio():
    print("🎵 --- Razi's Colab Audio Isolation System --- 🎵")
    
    # Prompt the user for the input file name
    input_mp3 = input("Enter the original audio file name (e.g., audio.mp3): ")
    
    # Determine device (GPU if available)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Demucs command for mp3 and vocals extraction
    command = f'python -m demucs -n htdemucs_ft -d {device} --mp3 --two-stems=vocals "{input_mp3}"'
    
    print(f"\n⚙️ Processing with {device.upper()}, please wait...")
    
    try:
        subprocess.run(command, shell=True, check=True)
        print("\n✅ Isolation successful! Files are in the 'separated' folder.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    process_audio()