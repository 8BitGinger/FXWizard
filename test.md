# FX Wizard: WebSocket Lower Third Overlay

![Logo](./assets/FxNoBack.png)

FX Wizard is a professional, customizable system for controlling animated lower-third graphics on an OBS stream using a web-based controller. It utilizes an internal Python WebSocket server to provide real-time communication between the controller and the display overlay.

## Table of Contents
- [✨ Features](#features)
- [🛠️ Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [💻 Usage](#usage)
    - [Controller View (Input)](#controller-view-input)
    - [Display View (OBS Source)](#display-view-obs-source)
- [📜 License](#license)
- [📧 Contact](#contact)
- [📷 Screenshots](#screenshots)
- [🔗 Links](#links)
- [🌟 Acknowledgements](#acknowledgements)

## ✨ Features

- **Integrated Python Server**: The WebSocket server runs directly inside OBS as a script, replacing the need for standalone terminal windows or Node.js background processes.
- **Real-time Control**: Instantly send text and positioning data to the OBS overlay via WebSockets.
- **Modern Studio UI**: Features a professional palette for high visibility with white text.
- **9-Point Grid Positioning**: Supports precise placement (Top/Center/Bottom, Left/Middle/Right) through a responsive location selector.
- **Preset Storage**: Save and manage frequently used lower-third combinations using Local Storage for quick recall.
- **Advanced Animations**: Built-in support for Slide Up, Slide Down, Slide Left, Slide Right, Spin In, and Fade transitions.

## 🛠️ Setup

### Prerequisites

- **OBS Studio**: Ensure you have OBS Studio installed with Python support enabled.
- **Python 3.10+**: A local installation of Python is required for the internal server logic.
- **Websockets Library**: The Python environment must have the `websockets` library installed.

### Installation Steps

1. **Install Dependencies**: Open your terminal or command prompt and run the following command to install the necessary library for the internal OBS server:
    ```bash
    python -m pip install websockets
    ```

2. **Load the Server into OBS**:
    - Place the `fx_wizard_server.py` script inside your `FXWizard` folder.
    - Open **OBS Studio** and navigate to **Tools** > **Scripts**.
    - In the **Python Settings** tab, ensure your local Python installation path is correctly linked.
    - In the **Scripts** tab, click the **+** button and select `fx_wizard_server.py`.
    - The script log will confirm: `FXWizard: Python WebSocket Server started successfully.`.

## 💻 Usage

### 1. Controller View (Input)

Access the controller interface by opening `websocket_demo.html` in your browser. The view will automatically load as the controller if no hash is present, or specifically via `#controller`.

- **Name/Title**: Input the primary label and smaller subtitle.
- **Duration**: Set how long the graphic remains visible (default is 5 seconds).
- **Animation and Font**: Choose the transition style (Slide, Spin, Fade) and font type.
- **Location**: Select the screen position using the 3x3 grid.
- **⚡ TAKE**: Sends the current graphic contents to the overlay immediately.
- **💾 SAVE**: Adds the current configuration to the "Saved Lowers" list for future use.

### 2. Display View (OBS Source)

This view is added to OBS as a **Browser Source** to show the animated graphics.

- **Access**: Open `websocket_demo.html#display`.
- **OBS Setup**:
    - Add a new **Browser Source** in OBS.
    - Check the **Local File** box and browse to `websocket_demo.html`.
    - In the URL field, ensure the hash `#display` is appended to the end of the path.
    - Set the width and height to match your OBS canvas (e.g., 1920x1080).
    - Ensure "Shutdown source when not active" is checked for optimal performance.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 📧 Contact

For questions or support, please contact the author at: [Gmail](mailto:ryan.fann@gmail.com) or visit the GitHub repository: [FXWizard](https://github.com/8bitginger/FXWizard).

## 📷 Screenshots

![Controller View](./assets/fxController.png)
*Controller View (Input)*

![Display View](./assets/fxDisplay2.png)
*Display View (OBS Source)*

## 🔗 Links

- [GitHub Repository](https://github.com/8bitginger/FXWizard)
- [MIT License](./LICENSE)
- [OBS Studio](https://obsproject.com/)

## 🌟 Acknowledgements

This project benefited from the assistance of Gemini, a large language model, in the following areas:

- **Architectural Design**: Guidance on integrating an internal Python WebSocket server into the OBS workflow.
- **Front-End Integration**: Assistance with Tailwind CSS utility styling for a responsive and modern controller interface.
- **Debugging and Diagnostics**: Identification and resolution of conflicts related to CSS animation timing and transform property interference.
- **Branding**: Generation of the FX Wizard Graphic [Logo](./assets/FxNoBack.png).