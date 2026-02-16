# FX Wizard: WebSocket Lower Third Overlay

![Logo](./assets/FxNoBack.png)

**FX Wizard** is a professional, customizable system for controlling animated lower-third graphics on an OBS stream using a web-based controller. It leverages WebSockets for real-time communication between the controller and the display.

You can run FX Wizard using either an **Internal Python Server** (runs inside OBS) or a **Standalone Node.js Server** (runs in the background).

---

## ✨ Features

- **Dual-Server Options**: Choose between an internal OBS Python script or a standalone Node.js environment.
- **Real-time Control**: Instantly send text and positioning data to the OBS overlay via WebSockets.
- **Modern Studio UI**: Optimized palette featuring **Indigo-600** (Save), **Rose-500** (Delete), and **Slate-700** (Selection) for high visibility.
- **9-Point Grid Positioning**: Precise placement (TL, CM, BR, etc.) through a responsive location selector.
- **Preset Storage**: Save frequently used lower-third combinations to Local Storage for quick recall.
- **Advanced Animations**: Built-in support for Slide, Spin In, and Fade transitions.

---

## 🛠️ Setup Option A: Internal Python Server (Recommended)

_Best for users who want the server to start and stop automatically with OBS Studio._

### 1. Prerequisites

- **OBS Studio** (with Python support enabled).
- **Python 3.11 (64-bit)** installed on your machine.
- The `websockets` library installed.

### 2. Installation

1.  **Install Library**: Open your terminal and run:
    ```bash
    python -m pip install websockets
    ```
2.  **DLL Fix**: Navigate to your Python install folder. Copy `python311.dll` and rename the copy to `python3.dll`. This allows OBS to correctly load the interpreter.
3.  **Load Script**:
    - Open OBS Studio > **Tools** > **Scripts**.
    - In **Python Settings**, link the path to your Python install folder (e.g., `C:\Program Files\Python311`).
    - In **Scripts**, click the **+** and add `server.py`.
4.  **Verify**: Check the script log for: `FXWizard: Server listening on ws://0.0.0.0:8080`.

---

## 🛠️ Setup Option B: Standalone Node.js Server

_Best for users who prefer a separate terminal process or external control._

### 1. Prerequisites

- **Node.js** installed on your machine.
- The `ws` library.

### 2. Installation

1.  **Install Dependencies**: Open your terminal in the project directory and run:
    ```bash
    npm install ws
    ```
2.  **Start the Server**:
    ```bash
    node server.js
    ```
    _Note: You may use the included `launch_server.bat` file to start the server with a double-click._

---

## 💻 Usage

Regardless of the server chosen, the front-end usage remains the same:

### 1. Controller View (Input)

Access the controller by opening `websocket_demo.html#controller` in your browser.

- **⚡ TAKE**: Sends the current graphic contents to the overlay immediately.
- **💾 SAVE**: Adds the current configuration to the "Saved Lowers" list.
- **Duration**: Set visibility time in seconds (default is 5s).
- **Selection**: Active choices are highlighted in **Slate-700** for high contrast.

### 2. Display View (OBS Source)

1.  Add a **Browser Source** in OBS.
2.  Check **Local File** and select `websocket_demo.html`.
3.  Append `#display` to the end of the file path.
4.  Set the resolution to match your canvas (e.g., 1920x1080).
5.  Ensure **"Shutdown source when not active"** is checked for optimal performance.

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

For support, contact the author at: **ryan.fann@gmail.com** or visit the GitHub repository: **FXWizard**

## 🌟 Acknowledgements

This project benefited from the assistance of Gemini, a large language model, in the following areas:

- **Architectural Design**: Transitioning to an internal Python WebSocket server for OBS.
- **UI Refinement**: Implementation of Tailwind CSS and studio-grade color palettes.
- **Debugging**: Resolving CSS animation conflicts and Python async loop errors.
- **Branding**: Generation of the FX Wizard Logo.
- **Gifs**: Used [EzGif](https://ezgif.com/video-to-gif) to transfer content from [Storyblocks](https://www.storyblocks.com/)
- **Fonts** [Google Fonts](https://fonts.google.com/)
