# session-keeper

Session Keeper is a Python-based utility designed to help Roblox developers and players maintain their in-game sessions. With this tool, you can automate session management, ensuring a seamless gaming experience without interruptions.

## Features

- **Automatic Session Recovery**: Automatically reconnect to your Roblox game session if it gets interrupted due to network issues or game crashes.
- **Customizable Idle Timeout**: Set personalized idle time limits, allowing the tool to monitor your activity and reconnect as needed.
- **User-Friendly Command Line Interface**: Launch and configure the application easily using straightforward commands and options.
- **Log Tracking**: Keep track of all session activities with detailed logs, offering insights into connection stability and session duration.

## Installation

To install Session Keeper, you need Python 3.7 or higher. Follow the steps below to get started:

1. Clone the repository:

    ```bash
    git clone https://github.com/Developer/session-keeper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd session-keeper
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Basic Usage

To start using Session Keeper, simply run the following command in your terminal:

```bash
python session_keeper.py --timeout 300
```

In the above command, `--timeout` sets the idle time limit to 300 seconds (5 minutes). Modify this value as needed to fit your gaming preferences.

For a list of all available options, run:

```bash
python session_keeper.py --help
```

This will display helpful information on additional configurations and commands to fine-tune your session management experience.

## License 

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.