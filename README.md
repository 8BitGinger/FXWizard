# FX Wizard: WebSocket Lower Third Overlay



![Logo](./assets/FxNoBack.png)



FX Wizard is a simple, customizable system for controlling animated lower-third graphics on an OBS stream (or any browser source) using a separate web controller interface. It leverages WebSockets for instant, real-time communication between the controller and the display.

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
- [🖥️ Running the batch file](#running-the-batch-file)
- [🌟 Acknowledgements](#acknowledgements)

## ✨ Features

- **WebSocket Communication**: Uses WebSockets for real-time updates between the controller and the display.
- **Real-time Control**: Instantly send text and positioning data to the OBS overlay via WebSockets.

- **Two-View System**: Separates the Controller (input/management) and the Display (OBS source).

- **Customizable Location**: Supports a 3x3 grid for precise placement of the graphic (Top/Center/Bottom, Left/Middle/Right).

- **Variable Duration**: Users can specify the exact time (in seconds) the lower third stays on screen before automatically fading out.

- **Preset Storage**: Save frequently used lower-third combinations (Name, Title, Location, Font, and Duration) using Local Storage for quick recall.
- **Customizable Fonts**: Includes options for default, script, and fun font styles.

<a id="setup"></a>

## 🛠️ Setup

### Prerequisites

- **Node.js**: Ensure you have Node.js installed on your machine. You can download it from [nodejs.org](https://nodejs.org/).
- **OBS Studio**: Download and install OBS Studio from [obsproject.com](https://obsproject.com/).
- **Repository Clone**: Clone the FX Wizard repository to your local machine.

### Installation Steps

1.  **Install Dependencies**: The project requires the `ws` WebSocket library. Open your terminal in the project directory and run this single command:
    ```bash
    npm install ws
    ```

2.  **Start the Server**: Launch the WebSocket server using Node.js.
    ```bash
    node server.js
    ```
    You should see the confirmation message: `WebSocket Server started on ws://localhost:8080.`. *(If you have modified the port in `server.js`, use the appropriate URL.)*

    > **Alternative Startup:** You may use the included `launch_server.bat` file to run the server in the background. If using this file, ensure the directory path inside the batch file is updated to match your local repository location. [***Click here for Instructions***](#running-the-batch-file) <br><br> ***Note: Keep this terminal window open while using the FX Wizard, as it runs the WebSocket server.***

     

<div id="usage"></div>

## ✨ Usage

The system is accessed via the websocket_demo.html file, using URL hashes to select the mode. The WebSocket server must be running before accessing either page.

<div id="controller-view-input"></div>

### 1. Controller View (Input)

This is the interface you use to manage and send graphics.

#### ***Functionality***

Primary/Secondary: Input the main name/label and the smaller title/subtitle.

Duration (sec): Set how long the graphic should remain visible (default is 5 seconds).

Animation and Font: Choose the animation style and font type.

Location: Select the desired position on the screen using the 3x3 grid.

⚡ Instant Send: Sends the current form contents immediately.

💾 Save Lower 3rd: Saves the current form contents as a reusable button in the "Saved Lowers" section below.

#### ***OBS Setup***

In OBS, add Custom Dock.
In the URL field, add the hash: file:///[path-to-file]/websocket_demo.html#controller

When you click a button in this Controller View, the graphic will appear in the Display View (as long as the browser source is added to the OBS scene) with a smooth animation and fade out after the set duration.

---

### 2. Display View (OBS Source)

This view is added to OBS as a Browser Source.
This is the view that shows the animated lower third graphic.

***Access:*** Open websocket_demo.html#display.

#### ***OBS Setup***

In OBS, add a new Browser Source.

Set the Local File checkbox.

Browse and select websocket_demo.html.

In the URL field, add the hash: file:///[path-to-file]/websocket_demo.html#display

Set your desired OBS source size (e.g., 1920x1080).

Check "Shutdown source when not active" and "Refresh browser when scene becomes active" for best performance.

Crucially, ensure the CSS property for the OBS source is transparent so only the lower third appears.

When you click a button in the Controller View, the graphic will appear in the Display View (and your OBS scene) with a smooth animation and fade out after the set duration.

<div id="license"></div>

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

<div id="contact"></div>

## 📧 Contact

For questions or support, please contact the author at: [Gmail](mailto:ryan.fann@gmail.com) or visit the GitHub repository: [FXWizard](https://github.com/8bitginger/FXWizard)

<div id="screenshots"></div>

## 📷 Screenshots

![Controller View](./assets/fxController.png)
*Controller View (Input)*

![Display View](./assets/fxDisplay2.png)
*Display View (OBS Source)*

<div id="links"></div>

## 🔗 Links

- [GitHub Repository](https://github.com/8bitginger/FXWizard)
- [MIT License](./LICENSE)
- [Node.js ws Library](https://www.npmjs.com/package/ws)
- [OBS Studio](https://obsproject.com/)


<div id="running-the-batch-file"></div>

## 🖥️ Running the batch file
To simplify the process of starting the WebSocket server, you can use the provided `launch_server.bat` file. Follow these steps:
1. **Update the Path**: Open `launch_server.bat` in a text editor and modify the `cd` command to point to the directory where you cloned the FX Wizard repository on your machine.
2. **Run the Batch File**: Double-click the `launch_server.bat` file to execute it. This will navigate to the project directory and start the Node.js server automatically.

> ***Note: Keep this terminal window open while using the FX Wizard, as it runs the WebSocket server.***

---

***Alternatively,*** you can create a permanent shortcut to the batch file on your desktop or taskbar for easier access.
1. Right-click the `launch_server.bat` file and select Send to > Desktop (create shortcut).

2. Right-click the new shortcut on your desktop and select Properties.

3. Go to the Shortcut tab.

4. Click the Advanced... button.

5. Check the box labeled **"Run as administrator".**

6. Click OK on all windows.

> ***Note: Keep this terminal window open while using the FX Wizard, as it runs the WebSocket server.***

---


<details>
  <summary>Task Scheduler Method (***Optional***):</summary>
  <p>
    You can also set up a Task Scheduler task to run the batch file at system startup with elevated privileges. Here’s how:
    <br>
    1. Open Task Scheduler (search for it in the Start menu).
    <br>
    2. Click on "Create Task..." in the Actions pane.
    <br>
    3. In the General tab, name your task (e.g., "FX Wizard Server") and check "Run with highest privileges."
    <br>
    4. In the Triggers tab, click "New..." and set the trigger to "At startup."
    <br>
    5. In the Actions tab, click "New..." and set the action to "Start a program." Browse to select your `launch_server.bat` file.
    <br>
    6. Click OK to save the task.
    This method will ensure that the WebSocket server starts automatically with your system, running in the background with the necessary permissions.
  </p>
</details>

<div id="acknowledgements"></div>

## 🌟 Acknowledgements

Acknowledgement of AI Assistance
This project benefited from the assistance of Gemini, a large language model, in the following areas:

### Technical Development and Refinement
---
Architectural Design and Code Modification: Provided guidance on integrating advanced functionality into the existing Node.js and WebSocket architecture. This included introducing support for multiple distinct animation styles (e.g., slide, fade).

Front-End Integration: Assisted with the implementation of Tailwind CSS utility styling within the websocket_demo.html controller interface to ensure responsiveness and clarity.

### Quality Assurance and Conflict Resolution
---
Critical Debugging and Diagnostics: Played a key role in identifying and resolving complex, low-level conflicts, specifically those related to CSS animation timing and transform property interference. This effort ensured that graphics faded out correctly after the specified duration without disrupting their on-screen position.

### Documentation and Presentation
---
Project Documentation: Generated the foundational structure and refined the language for the project's README file, ensuring clear instructions for setup and usage.

Media and Branding: Generated the FX Wizard Graphic [Logo](./assets/FXWizardLogo.png)