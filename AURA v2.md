# AURA v2

> The second generation of Aura, introducing encrypted persistent memory and a password-protected Redx Mode.

Aura v2 is a major evolution of the original Aura assistant.

While Aura v1 focused on basic command processing and temporary in-session memory, Aura v2 introduces persistent encrypted memory, cryptographic key management, password-based Redx Mode authentication, and a dedicated Redx Command Center.

Aura v2 remains a lightweight Python desktop assistant, but its architecture moves beyond simple runtime state and into file-based encrypted persistence.

---

# What's New in Aura v2

## 🔐 Encrypted Persistent Memory

Aura v2 stores memory on disk instead of keeping it only in RAM.

Memory is:

- Stored as JSON data
- Encrypted before being written to disk
- Loaded automatically when Aura starts
- Persistent between application sessions

The encrypted memory file is:

```text
redx_memory.enc
```

---

## 🔑 Cryptographic Memory Key

Aura uses a Fernet encryption key to protect memory.

The memory key is stored in:

```text
redx_key.key
```

If the key does not exist, Aura automatically generates one.

---

## 🔴 Password-Protected Redx Mode

Redx Mode is protected using a separate encrypted key system.

The protected key file is:

```text
redx_key_protected.key
```

The user enters a password through a protected input dialog.

Aura derives a cryptographic key from the supplied password and attempts to decrypt the protected Redx key.

If successful, Redx Mode is activated.

---

## 🧠 Persistent Memory Commands

Aura can store information using:

```text
remember <key> <value>
```

Example:

```text
remember project Aura
```

Aura stores the information and encrypts it before saving it to disk.

Information can later be retrieved using:

```text
recall <key>
```

Example:

```text
recall project
```

---

## 🛡️ Redx Command Center

Successful Redx Mode activation opens a dedicated command center containing experimental tools.

Current tools include:

- Activate Digital Shield
- Enable Stealth Protocols
- Purge Memory
- Scan for Threats

Some tools currently act as prototype command simulations and log status messages.

The Memory Purge tool performs an actual memory operation.

---

# Features

## 💬 Command-Based Interaction

Aura accepts commands through:

- A text input field
- The Enter key
- An Execute button

---

## 👋 Greeting Detection

Aura responds to commands containing:

```text
hello
```

---

## 🧠 Persistent Memory

Store information:

```text
remember <key> <value>
```

Retrieve information:

```text
recall <key>
```

Memory is encrypted and stored locally.

---

## 🔐 Encrypted Storage

Aura uses:

```text
Fernet Encryption
```

to encrypt memory data before writing it to disk.

---

## 🔴 Redx Mode Authentication

Redx Mode can be activated using:

```text
activate redx
```

or through the graphical interface.

---

# Technology Stack

## Programming Language

```text
Python
```

## GUI Framework

```text
Tkinter
```

## Encryption

```text
cryptography.fernet
```

## Data Format

```text
JSON
```

## Cryptographic Components

Aura v2 uses:

- SHA-256
- Base64 URL-safe encoding
- Fernet symmetric encryption

---

# Requirements

Aura v2 requires Python 3 and the following package:

```text
cryptography
```

Install it using:

```bash
pip install cryptography
```

Tkinter is included with many Python installations.

---

# Installation

Clone or download the Aura v2 project.

The expected project files are:

```text
Aura-v2/
│
├── aura_gen2.py
├── keygen.py
├── redx_key.key
├── redx_key_protected.key
└── redx_memory.enc
```

Install the required dependency:

```bash
pip install cryptography
```

Run Aura:

```bash
python aura_gen2.py
```

On some systems:

```bash
python3 aura_gen2.py
```

---

# Initial Setup

Aura v2 uses multiple files for encryption and Redx Mode.

## Generate a Protected Redx Key

The project includes:

```text
keygen.py
```

This script generates a Fernet key and encrypts it using a password-derived key.

Run:

```bash
python keygen.py
```

The script creates:

```text
redx_key_protected.key
```

---

# Basic Commands

| Command | Function |
|---|---|
| `hello` | Returns an Aura greeting |
| `remember <key> <value>` | Stores encrypted persistent memory |
| `recall <key>` | Retrieves stored memory |
| `activate redx` | Attempts to activate Redx Mode |

---

# Example Usage

## Store Memory

```text
remember creator Redx
```

Aura saves:

```text
creator → Redx
```

The data is encrypted before being written to the memory file.

---

## Recall Memory

```text
recall creator
```

Aura retrieves the stored value.

---

## Activate Redx Mode

```text
activate redx
```

Aura displays a password dialog.

If authentication succeeds:

```text
[REDX MODE ACTIVATED]
```

Aura then opens the Redx Command Center.

---

# Redx Command Center

The Redx Command Center is a separate graphical window.

It currently provides four tools.

## Activate Digital Shield

Displays:

```text
Digital Shield Activated.
```

This is currently a simulated command.

---

## Enable Stealth Protocols

Displays:

```text
Stealth Protocols Online.
```

This is currently a simulated command.

---

## Purge Memory

This tool:

1. Clears Aura's memory dictionary
2. Saves the empty memory structure
3. Overwrites the encrypted memory storage

This permanently removes stored Aura memory unless a backup exists.

---

## Scan for Threats

Displays a simulated scanning message.

Current implementation:

```text
Scanning for hostile traces... none found.
```

This is not a real malware scanner or system security scanner.

---

# Project Structure

```text
Aura-v2/
│
├── aura_gen2.py
│   └── Main Aura application
│
├── keygen.py
│   └── Protected Redx key generator
│
├── redx_key.key
│   └── Fernet key used for encrypted Aura memory
│
├── redx_key_protected.key
│   └── Password-protected Redx key
│
└── redx_memory.enc
    └── Encrypted persistent Aura memory
```

---

# Architecture

```text
                ┌──────────────┐
                │     User     │
                └──────┬───────┘
                       │
                       ▼
              ┌─────────────────┐
              │   Aura GUI      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Command Engine  │
              └────────┬────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
      Greeting      Memory        Redx Mode
                      │             │
                      ▼             ▼
                 Encryption    Authentication
                      │             │
                      ▼             ▼
              Encrypted File   Command Center
```

---

# Limitations

Aura v2 is more advanced than Aura v1, but several limitations remain.

- No natural language AI model
- No internet access
- No voice interaction
- No persistent conversation context beyond key-value memory
- No database backend
- No real threat detection
- Digital Shield and Stealth Protocols are simulated
- Memory key storage is file-based
- Redx Mode authentication does not currently implement rate limiting
- No command plugin system
- No structured logging system

---

# Security Notes

Aura v2 introduces genuine encryption, but it should not be treated as a production security system.

The application improves significantly over Aura v1 by:

- Encrypting persistent memory
- Using Fernet cryptography
- Separating protected Redx authentication data
- Deriving encryption material from passwords using SHA-256

However, future versions should consider:

- Strong password hashing and key derivation
- PBKDF2, scrypt, or Argon2 for password-derived keys
- Salted password processing
- Secure OS credential storage
- Rate limiting authentication attempts
- Memory key separation
- Backup and recovery mechanisms

---

# Version Information

```text
Project: Aura
Generation: 2
Version: v2.0
Language: Python
GUI: Tkinter
Memory: Persistent and Encrypted
Encryption: Fernet
Authentication: Password-Based Redx Mode
Storage: Local Files
Internet Access: No
AI Model: No
```

---

# Project Evolution

```text
Aura v1
│
├── Basic Command Processing
├── Temporary Memory
├── Simple Redx Mode
└── Single-File Architecture
        │
        ▼
Aura v2
│
├── Persistent Memory
├── Encrypted Storage
├── Cryptographic Keys
├── Password-Based Authentication
├── Redx Command Center
└── Multi-File Architecture
```

Aura v2 represents the transition from a simple prototype assistant into a more structured system with persistent state and cryptographic protection.

---

# Creator

Developed by **Redx**

---

# Aura Project

Aura v2 is the second generation of the Aura project.

The focus of this generation is clear:

```text
Persistence
+
Encryption
+
Authentication
+
Desktop Interaction
```

It is the point where Aura stopped being just a temporary command assistant and started developing an actual system architecture.