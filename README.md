# DeFidelity
DeFidelity is used to mass-decrease fidelity of WAV files recursively in subdirectories. 

## Example usage

```
Enter the directory to search for WAV files: /path/to/wav/files

Choose a sample rate for compression:
1: CD quality (44.1 kHz) - minimal compression
2: Broadcast quality (32 kHz) - moderate compression
3: Medium quality (22.05 kHz) - good compression
4: Low quality (16 kHz) - strong compression
5: Telephone quality (8 kHz) - extreme compression

Enter the number corresponding to your choice: 3

Starting compression with sample rate: 22050 Hz...
Compressed and replaced: /path/to/wav/files/audio1.wav
Compressed and replaced: /path/to/wav/files/subfolder/audio2.wav

Compression complete!
```
