# SHA-256 Cryptographic Hash Engine

This repository contains a fully functional, from-scratch implementation of the SHA-256 cryptographic hash algorithm. It is written in pure Python without using any external cryptographic libraries like hashlib.


---

## (a) Introduction to SHA-256

**What it is ?:**
SHA-256 (Secure Hash Algorithm 256-bit) is a **deterministic**, **one-way** cryptographic function (has **irreversible** nature). No matter the size of the input data—whether it is a single letter or a massive text file—the algorithm processes it and outputs a unique (tries to be *approximate* injectivity), fixed-size 256-bit digest, typically represented as a 64-character hexadecimal string. It is designed to be highly sensitive, changing even a single bit of the input completely scrambles the resulting hash (this is called the **avalanche** effect).

**Where it is used ?:**
* **Digital Signatures & Certificates:** Ensuring data has not been tampered with during transmission. It provides Integrity and authorization to the data received
* **Blockchain Technology:** Serving as the mathematical foundation for Bitcoin's Proof-of-Work mining and securing block headers.
* **Password Verification:** Safely storing user credentials in databases.

---

## (b) Implementation Details

I built this engine with a focus on mathematical accuracy and clean software architecture. The logic, as instructed, is separated into a mathematical function implementations library (`utils.py`) and a file with main implementation loop (`sha256.py`). The algorithm operates on the raw bit level, utilizing Python's integer byte conversion to simulate 32-bit hardware architectures.

**Key Steps in the Algorithm:**

* **Preprocessing & Padding:** Theoritically the input string is converted to raw strings of zero's and ones. A single `1` bit is appended, followed by enough `0` bits to pad the message. Finally, the exact bit-length of the original message is attached at the end so the entire payload is a perfect multiple of 512 bits but while implementing the algorithm I felt it was easier to work with bytes due to the convinience of using a bytearray while working in bytes.
* **The Message Schedule:** Theritically each 512-bit chunk is broken down into sixteen 32-bit words but following the bytes wise implementation I divided the 64 byte chunk into 16 , 4 byte words then I implemented the standard Sigma bitwise rotation and shift functions to mathematically expand these 16 words into a massive 64-word schedule.
* **The Compression Loop:** The core engine initializes eight working variables (A through H) using the fractional parts of the square roots of the first 8 prime numbers. The algorithm then runs a 64-round loop, applying bitwise logic (Majority, Choice, and Big Sigma functions) alongside the 64 generated words and prime-derived constants to irreversibly scramble the data.

---

## (c) How to Run the Code

since this project only contains python files the projected can be easily demonstrated on a terminal. 
just open the main.py file in the terminal by `python main.py` command to get the hash of any function you like ir just run the test file that has pre-written test cases to test/compare the output of this code with the one from the hashlib library

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

