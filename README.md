# SHA-256 Cryptographic Hash Engine

This repository contains a fully functional, from-scratch implementation of the SHA-256 cryptographic hash algorithm. It is written in pure Python and strictly adheres to the mathematical specifications outlined in the FIPS 180-4 standard, without relying on any external cryptographic libraries.

---

## (a) Introduction to SHA-256

**What it is:**
SHA-256 (Secure Hash Algorithm 256-bit) is a deterministic, one-way cryptographic function. No matter the size of the input data—whether it is a single letter or a massive text file—the algorithm processes it and outputs a unique, fixed-size 256-bit signature, typically represented as a 64-character hexadecimal string. It is designed to be highly sensitive; changing even a single bit of the input completely scrambles the resulting hash (an effect known as the avalanche effect).

**Where it is used:**
* **Digital Signatures & Certificates:** Ensuring data has not been tampered with during transmission.
* **Blockchain Technology:** Serving as the mathematical foundation for Bitcoin's Proof-of-Work mining and securing block headers.
* **Password Verification:** Safely storing user credentials in databases.
* **SSL/TLS Protocols:** Securing connections over the internet.

---

## (b) Implementation Details

I built this engine with a focus on mathematical accuracy and clean software architecture. Rather than writing a single massive script, the logic is separated into a mathematics library (`utils.py`) and a core compression engine (`sha256.py`). The algorithm operates on the raw bit level, utilizing Python's integer byte conversion to simulate 32-bit hardware architectures.

**Key Steps in the Algorithm:**

* **Preprocessing & Padding:** The input string is converted to raw bytes. A single `1` bit is appended, followed by enough `0` bits to pad the message. Finally, the exact bit-length of the original message is attached at the end so the entire payload is a perfect multiple of 512 bits.
* **The Message Schedule:** Each 512-bit chunk is broken down into sixteen 32-bit words. I implemented the standard Sigma bitwise rotation and shift functions to mathematically expand these 16 words into a massive 64-word schedule.
* **The Compression Loop:** The core engine initializes eight working variables (A through H) using the fractional parts of the square roots of the first 8 prime numbers. The algorithm then runs a 64-round loop, applying bitwise logic (Majority, Choice, and Big Sigma functions) alongside the 64 generated words and prime-derived constants to irreversibly scramble the data.

---

## (c) How to Run the Code

This project runs via a Command Line Interface (CLI) and requires no external installations or dependencies. 

1. Ensure Python 3 is installed on your system.
2. Open your terminal or command prompt.
3. Navigate to the folder containing the project files.
4. Run the following command to launch the user interface:
   `python main.py`
5. Type your message when prompted and press Enter to generate the hash.

---

## (d) Example Inputs and Outputs

Below are standard test cases verifying the deterministic nature of the algorithm:

**Input:** *(Empty String)*
**Output:** `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

**Input:** `abc`
**Output:** `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`

**Input:** `Mallhar`
**Output:** `34f8a37f59d584ab8d2aab24fb142a78127f8a7042a3cf2179f826352ea2a1a0`

---

## (e) Special Functionalities

* **Automated FIPS Verification Suite:** I built a custom test script (`test.py`) that strictly validates this implementation. It pits my mathematical engine against Python's official, highly optimized `hashlib` C-library. It runs through edge cases (empty strings, standard strings, and multi-block overflows) to mathematically prove the hashes match the official FIPS standard byte-for-byte. To run it, execute `python test.py`.
* **Separation of Concerns:** The code features a professional 4-file architecture (`utils.py`, `sha256.py`, `main.py`, `test.py`) separating the math, the core engine, the UI, and the testing suite. This ensures the `sha256.py` engine can be seamlessly imported into future projects without triggering terminal prompts.
* **32-bit Hardware Overflow Simulation:** Because Python integers expand infinitely, I engineered a bitwise mask (`& 0xFFFFFFFF`) applied to all addition operations to strictly simulate hardware-level 32-bit modulo arithmetic, ensuring true cryptographic compliance.
