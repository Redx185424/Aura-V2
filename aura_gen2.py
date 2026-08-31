import os
import json
import base64
import hashlib

import tkinter as tk
from tkinter import messagebox, simpledialog

from cryptography.fernet import Fernet, InvalidToken


# ============================================================
# REDX KEY / AUTHENTICATION SYSTEM
# ============================================================

def derive_key(password: str) -> bytes:
    """Derive a valid Fernet key from a password."""
    return base64.urlsafe_b64encode(
        hashlib.sha256(password.encode("utf-8")).digest()
    )


def load_redx_key(password: str):
    """Unlock the protected Redx key using the supplied password."""
    try:
        with open("redx_key_protected.key", "rb") as f:
            encrypted_key = f.read()

        fernet = Fernet(derive_key(password))
        return fernet.decrypt(encrypted_key)

    except FileNotFoundError:
        messagebox.showerror(
            "Redx Mode Error",
            "redx_key_protected.key was not found."
        )

    except InvalidToken:
        messagebox.showerror(
            "Access Denied",
            "Incorrect Redx Mode password."
        )

    return None


# ============================================================
# ENCRYPTED MEMORY SYSTEM
# ============================================================

KEY_PATH = "redx_key.key"
DATA_PATH = "redx_memory.enc"


def load_or_create_memory_key() -> bytes:
    """Load the existing Aura memory key or create one."""
    if os.path.exists(KEY_PATH):
        with open(KEY_PATH, "rb") as key_file:
            return key_file.read()

    new_key = Fernet.generate_key()

    with open(KEY_PATH, "wb") as key_file:
        key_file.write(new_key)

    return new_key


memory_key = load_or_create_memory_key()
cipher = Fernet(memory_key)


def encrypt_data(data_dict: dict) -> bytes:
    """Encrypt Aura memory."""
    json_data = json.dumps(data_dict).encode("utf-8")
    return cipher.encrypt(json_data)


def decrypt_data(enc_data: bytes) -> dict:
    """Decrypt Aura memory safely."""
    try:
        json_data = cipher.decrypt(enc_data)
        return json.loads(json_data.decode("utf-8"))

    except (InvalidToken, ValueError, json.JSONDecodeError):
        return {}


def save_memory(memory: dict):
    """Save encrypted Aura memory to disk."""
    with open(DATA_PATH, "wb") as f:
        f.write(encrypt_data(memory))


def load_memory() -> dict:
    """Load encrypted Aura memory."""
    if not os.path.exists(DATA_PATH):
        return {}

    try:
        with open(DATA_PATH, "rb") as f:
            return decrypt_data(f.read())

    except OSError:
        return {}


memory = load_memory()


# ============================================================
# MAIN AURA APPLICATION
# ============================================================

redx_mode_active = False


def log_msg(msg: str):
    log.insert(tk.END, f"> {msg}\n")
    log.see(tk.END)


def activate_redx_mode():
    """Ask for the Redx password and unlock Redx Mode."""
    global redx_mode_active

    if redx_mode_active:
        log_msg("Redx Mode is already active.")
        return

    password = simpledialog.askstring(
        "Redx Mode",
        "Enter Redx Mode password:",
        show="*",
        parent=root
    )

    if not password:
        return

    unlocked_key = load_redx_key(password)

    if unlocked_key:
        redx_mode_active = True
        log_msg("[REDX MODE ACTIVATED]")
        log_msg("Protected Redx key unlocked.")

        open_redx_command_center()


def open_redx_command_center():
    """Open the Redx command center."""

    def tool_1():
        log_msg("Digital Shield Activated.")

    def tool_2():
        log_msg("Stealth Protocols Online.")

    def tool_3():
        memory.clear()
        save_memory(memory)
        log_msg("Memory Purged.")

    def tool_4():
        log_msg("Scanning for hostile traces... none found.")

    redx_window = tk.Toplevel(root)
    redx_window.title("Redx Command Center")
    redx_window.geometry("300x260")

    tk.Label(
        redx_window,
        text="Redx Tools",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    tk.Button(
        redx_window,
        text="Activate Digital Shield",
        command=tool_1
    ).pack(pady=4)

    tk.Button(
        redx_window,
        text="Enable Stealth Protocols",
        command=tool_2
    ).pack(pady=4)

    tk.Button(
        redx_window,
        text="Purge Memory",
        command=tool_3
    ).pack(pady=4)

    tk.Button(
        redx_window,
        text="Scan for Threats",
        command=tool_4
    ).pack(pady=4)


def process_command(cmd: str):
    command = cmd.strip()

    if not command:
        return

    lower_command = command.lower()

    if "hello" in lower_command:
        log_msg("Hello, I am Aura. Awaiting instructions.")

    elif lower_command.startswith("remember "):
        parts = command.split(maxsplit=2)

        if len(parts) < 3:
            log_msg("Usage: remember <key> <value>")
            return

        _, memory_name, memory_value = parts

        memory[memory_name] = memory_value
        save_memory(memory)

        log_msg(f"Memory saved for key '{memory_name}'.")

    elif lower_command.startswith("recall "):
        parts = command.split(maxsplit=1)

        if len(parts) < 2:
            log_msg("Usage: recall <key>")
            return

        memory_name = parts[1]
        value = memory.get(memory_name, "Not found.")

        log_msg(f"{memory_name}: {value}")

    elif lower_command == "activate redx":
        activate_redx_mode()

    else:
        log_msg("Unknown command.")


def run_command():
    cmd = entry.get()

    if cmd.strip():
        log_msg(cmd)
        process_command(cmd)

    entry.delete(0, tk.END)


# ============================================================
# SINGLE TKINTER APPLICATION
# ============================================================

root = tk.Tk()
root.title("Aura Gen 2")
root.geometry("520x460")

title = tk.Label(
    root,
    text="AURA GEN 2",
    font=("Arial", 16, "bold")
)
title.pack(pady=(12, 4))

subtitle = tk.Label(
    root,
    text="Encrypted Memory and Redx Mode"
)
subtitle.pack(pady=(0, 10))

log = tk.Text(root, height=18, width=62)
log.pack(padx=10, pady=5)

entry = tk.Entry(root, width=55)
entry.pack(padx=10, pady=(8, 4))
entry.bind("<Return>", lambda event: run_command())

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(
    button_frame,
    text="Execute",
    command=run_command
).pack(side=tk.LEFT, padx=4)

tk.Button(
    button_frame,
    text="Activate Redx Mode",
    command=activate_redx_mode
).pack(side=tk.LEFT, padx=4)


log_msg(
    "Aura initialized. Commands: hello, remember <key> <value>, "
    "recall <key>, activate redx"
)

root.mainloop()
