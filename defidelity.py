import os
from pydub import AudioSegment


def compress_and_replace_wav(input_file, sample_rate):
    """
    Compress a WAV file by reducing its sample rate and replace the original.

    :param input_file: Path to the input WAV file
    :param sample_rate: New sample rate (e.g., 22050 for 22.05 kHz)
    """
    try:
        # Load the original WAV file
        audio = AudioSegment.from_file(input_file, format="wav")
        # Resample the audio with the specified sample rate
        audio = audio.set_frame_rate(sample_rate)
        # Create a temporary file path for the compressed WAV
        temp_file = input_file + ".tmp.wav"
        # Export the modified audio as a WAV file
        audio.export(temp_file, format="wav")
        # Replace the original file
        os.remove(input_file)  # Delete the original WAV file
        os.rename(temp_file, input_file)  # Rename the temp file to the original name
        print(f"Compressed and replaced: {input_file}")
    except Exception as e:
        print(f"Failed to compress {input_file}: {e}")


def find_and_compress_wav_files(base_directory, sample_rate):
    """
    Recursively find all WAV files in subdirectories and compress them in-place.

    :param base_directory: Root directory to search for WAV files
    :param sample_rate: New sample rate for compression
    """
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file.lower().endswith(".wav"):
                input_path = os.path.join(root, file)
                compress_and_replace_wav(input_path, sample_rate)


def guided_experience():
    """
    Guide the user through selecting a directory and a sample rate for compression.
    """
    print("Welcome to the WAV Compressor!")

    # Step 1: Ask for the directory to search for WAV files
    while True:
        base_dir = input("Enter the directory to search for WAV files: ").strip()
        if os.path.isdir(base_dir):
            break
        else:
            print("Invalid directory. Please enter a valid path.")

    # Step 2: Offer sample rate choices
    print("\nChoose a sample rate for compression:")
    sample_rate_choices = {
        1: (44100, "CD quality (44.1 kHz) - minimal compression"),
        2: (32000, "Broadcast quality (32 kHz) - moderate compression"),
        3: (22050, "Medium quality (22.05 kHz) - good compression"),
        4: (16000, "Low quality (16 kHz) - strong compression"),
        5: (8000, "Telephone quality (8 kHz) - extreme compression")
    }
    for key, (rate, description) in sample_rate_choices.items():
        print(f"{key}: {description}")

    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if choice in sample_rate_choices:
                sample_rate = sample_rate_choices[choice][0]
                break
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Step 3: Start compression
    print(f"\nStarting compression with sample rate: {sample_rate} Hz...")
    find_and_compress_wav_files(base_dir, sample_rate)
    print("\nCompression complete!")


if __name__ == "__main__":
    guided_experience()
