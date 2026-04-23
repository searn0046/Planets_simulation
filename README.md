# Planet Simulation

My ever-so-slightly different implementation of Tech With Tim's "Planet Simulation In Python" tutorial on YouTube.

All credits to Tech With Tim.
Original code: https://github.com/techwithtim/Python-Planet-Simulation

## Requirements

- Python 3.10+ (recommended)
- pip

## Project Structure

```text
classes.py
config.py
main.py
requirements.txt
```

## Setup

### 1. Open a terminal in the project folder

```bash
cd Planets_simulation
```

### 2. Create and activate a virtual environment

#### macOS / Linux

Create the environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

#### Windows (PowerShell)

Create the environment:

```powershell
python -m venv .venv
```

If script execution is blocked, allow it for the current PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Simulation

With the virtual environment activated:

```bash
python main.py
```

If that does not work on your system, try:

```bash
python3 main.py
```

## Controls

- Close the window or press your system close button to quit.
- Press `Esc` while in fullscreen mode to toggle fullscreen.

## Deactivate Virtual Environment

When you are done:

```bash
deactivate
```
