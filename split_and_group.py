import subprocess

def extract_compress_audio():
    print("\n--- 🎧 Extract & Compress Audio ---")
    video_path = input("Enter original video file name (e.g., video.mp4): ")
    output_mp3 = input("Enter output audio file name (e.g., output.mp3): ")
    
    # Command to extract and highly compress audio
    cmd = f'ffmpeg -i "{video_path}" -vn -c:a libmp3lame -q:a 5 "{output_mp3}" -y'
    
    print("\n⚙️ Extracting and compressing audio...")
    subprocess.run(cmd, shell=True, check=True)
    print("✅ Audio extracted and saved successfully!")

def merge_audio_video():
    print("\n--- 🎬 Merge Audio & Video ---")
    video_path = input("Enter original video file name: ")
    audio_path = input("Enter clean audio file name: ")
    output_video = input("Enter final video file name (e.g., final.mp4): ")
    
    # Ultimate fix: re-encode video with superfast preset for perfect sync
    cmd = f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v libx264 -preset superfast -crf 18 -c:a aac -map 0:v:0 -map 1:a:0 -pix_fmt yuv420p -shortest "{output_video}" -y'
    
    print("\n⚙️ Merging and syncing video with audio (this may take a few moments)...")
    subprocess.run(cmd, shell=True, check=True)
    print("✅ Merged successfully! Synchronization is now 100% perfect.")

def main():
    print("🛠️ --- Razi's Local FFmpeg Tools --- 🛠️")
    print("1. Extract audio from video (Compressed MP3)")
    print("2. Merge audio with video (Ultimate sync fix)")
    
    choice = input("\n👉 Enter the operation number (1 or 2): ")
    
    if choice == '1':
        extract_compress_audio()
    elif choice == '2':
        merge_audio_video()
    else:
        print("\n❌ Invalid choice!")

if __name__ == "__main__":
    main()