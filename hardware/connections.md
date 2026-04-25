# 🔗 Hardware Connections — Smart Door Lock System

## 📌 Overview

This section describes how the hardware components are connected in the Smart Door Lock System. The connections are based on the actual implementation of the project using Raspberry Pi Pico, Servo Motor, and PIR Sensor.

---

## 🔌 Connections Description

### 🔹 Servo Motor Connections

- Signal (Orange/Yellow) → GPIO Pin GP5  
- VCC (Red) → 5V / 3.3V  
- GND (Brown/Black) → GND  

### 🧠 Explanation

- The servo motor is responsible for locking and unlocking the door  
- It is controlled using PWM signals from the Raspberry Pi Pico  
- Different angles represent:
  - Lock position  
  - Unlock position  

---

### 🔹 PIR Sensor Connections

- VCC → 3.3V  
- GND → GND  
- OUT → GPIO Pin GP6  

### 🧠 Explanation

- PIR sensor detects motion using infrared radiation  
- When motion is detected:
  - Output becomes HIGH  
- The Pico reads this signal and can trigger actions  

---

### 🔹 Power Supply

- Raspberry Pi Pico is powered using a USB cable  
- USB provides:
  - Power supply  
  - Programming interface  

---

## 📸 Complete Hardware Setup

  - Door Open State
<img width="657" height="726" alt="image" src="https://github.com/user-attachments/assets/fa803aa6-ddd9-4b2c-aa07-2103f6b16055" />
  <br>

  - Door Closed State
<img width="662" height="718" alt="image" src="https://github.com/user-attachments/assets/f3ea9c58-53a8-4265-ae21-9d4c45afdc7b" />
  <br>
*Figure: Physical model of the Smart Door Lock System (as shown in the project report)*

---

## 🔁 Circuit Diagram

<img width="553" height="437" alt="image" src="https://github.com/user-attachments/assets/241c4c71-7b4b-4dbd-9014-906bbdfadae6" />

*Figure: Circuit diagram showing connections between Raspberry Pi Pico, Servo Motor, and PIR Sensor*

---

## ⚠️ Important Notes

- Ensure correct GPIO pins match the program code  
- Maintain proper grounding across all components  
- Use stable power supply for servo motor  
- Loose wiring may cause unstable behavior  

---

## 🧠 Working Insight

- User sends command through web interface  
- Raspberry Pi Pico processes the request  
- Servo motor performs locking/unlocking action  
- PIR sensor continuously monitors motion  

---

## 📌 Note

Detailed connection diagrams (individual wiring images) are not included in the original project report. The connections above are described based on the implemented system.

---

## 📌 Summary

The system integrates sensing (PIR sensor), processing (Raspberry Pi Pico), and actuation (servo motor) through proper wiring. Accurate connections ensure reliable operation of the smart door lock system.
