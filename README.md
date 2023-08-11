# Warehouse Automation
Warehouse Automation is a comprehensive project that streamlines warehouse operations through the integration of software and hardware components. This system enhances efficiency and accuracy in managing inventory and order fulfillment processes.

## Components
### 1. Arduino Control
The Arduino control section consists of two parts:
- Belt Control: Upload the Belt.ino code to manage and control the conveyor belt system, ensuring seamless movement of goods within the warehouse.
- ASRS Control: Upload the ASRS.ino code to oversee the Automated Storage and Retrieval System (ASRS). Inside the ASRS folder, you'll find additional files including ASRSw/Queue.ino, which facilitates ASRS testing with a queue, enabling runtime comparison with simulations.
### 2. Warehouse Management System (WMS)
The Warehouse Management System is a crucial software component that orchestrates the entire warehouse automation process. To get started:
1. Navigate to the WMS folder.
2. Modify the path in the WMS.py file to match your system's configuration.

## Getting Started
To implement Warehouse Automation on your setup, follow these steps:
1. Clone this repository to your local environment.
2. Install the necessary dependencies:
- PyQt5
- qrcode
- serial
- time
- sys
- os
- sqlite3
- threading
### Use pip to install the required packages:
- pip install pyqt5 qrcode[pil] pyserial
3. Set up the Arduino components by uploading the appropriate .ino files as described above.
4. Configure the Warehouse Management System by updating the path in the WMS.py file to align with your system's layout.
5.Run the Warehouse Management System:
- python WMS.py
## Arduino Control
The Arduino control section is designed to optimize warehouse processes. It offers control over the conveyor belt and the Automated Storage and Retrieval System (ASRS). By coordinating these elements, the system enhances overall efficiency and reduces operational errors.

