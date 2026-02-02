# Cryptographic Hashing Benchmarks 

A performance and security analysis tool written in Python to evaluate various hashing algorithms.

## Project Overview
This tool benchmarks the computational cost and security characteristics of different hashing algorithms, specifically focusing on the **Avalanche Effect** and resistance to brute-force attacks.

## Features
* **Avalanche Effect Analysis:** visualizes how a 1-bit change in input drastically alters the hash output.
* **Performance Benchmarking:** Measures the time cost (ms) for generating hashes.
* **Algorithms Tested:**
  * `MD5` (Fast, insecure)
  * `SHA-256` (Standard security)
  * `Bcrypt` (Slow, resistant to brute-force)

## Built With
* Python 3.10
* Library: `hashlib`
* Library: `bcrypt`
