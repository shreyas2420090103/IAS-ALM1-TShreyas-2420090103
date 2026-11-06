# IAS ALM1 — Encryption Algorithms and File Handling

**Student:** T. Shreyas Reddy  
**Roll Number:** 2420090103

This repository contains the files transferred, with permission, from [Gokul485/IAS-ALM1-Gokul-2420090027](https://github.com/Gokul485/IAS-ALM1-Gokul-2420090027).

## Project contents

- `algorithms/caesar_cipher.py` — Caesar cipher encryption and decryption.
- `algorithms/playfair_cipher.py` — Playfair cipher encryption.
- `algorithms/sdes.py` — Simplified DES encryption and decryption.
- `create_file.py` — Generates a sample 10 KB text file in the `files/` directory.

## Requirements

- Python 3
- No third-party Python packages are required.

## Run the programs

From the repository root, run:

```bash
python algorithms/caesar_cipher.py
python algorithms/playfair_cipher.py
python algorithms/sdes.py
```

To create the sample 10 KB file, first create the output directory and then run:

```bash
mkdir files
python create_file.py
```

## Note

The upstream README mentions a TCP client/server transfer component and screenshots, but those files are not present in the source repository's tracked file tree. They were therefore not included in this transfer. The cipher implementations here are educational demonstrations and should not be used to protect real data.
