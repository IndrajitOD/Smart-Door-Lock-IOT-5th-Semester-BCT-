# 🔌 Hardware Components — Smart Door Lock System

## 📌 Overview

This project uses a combination of embedded hardware components to implement a smart door locking mechanism with IoT capabilities. Each component plays a specific role in sensing, processing, communication, or actuation, forming a complete and functional embedded system.

---

## 🧩 Components List

### 🔹 1. Raspberry Pi Pico  
  <img width="387" height="195" alt="Screenshot 2026-04-26 024216" src="https://github.com/user-attachments/assets/86b4fb2f-ec3b-4688-8095-95ea75583747" />

- Microcontroller based on RP2040 dual-core ARM Cortex-M0+  
- Acts as the central processing unit of the system  
- Handles sensor input, networking, and actuator control  
- Supports MicroPython programming for rapid development  
- Provides multiple GPIO pins for interfacing with sensors and actuators  
- Low-cost and energy-efficient, suitable for embedded applications  

---

### 🔹 2. Micro Servo Motor  
  <img width="390" height="210" alt="image" src="https://github.com/user-attachments/assets/a98bbd02-9ec8-46c1-b85d-933e81eb7136" />

- Used for physical locking and unlocking mechanism  
- Controlled using PWM (Pulse Width Modulation) signals  
- Rotates to predefined angles:
  - 0° → Lock position  
  - 90° → Unlock position  
- Provides precise angular control  
- Compact size makes it suitable for small-scale automation projects  
- Requires stable power supply for consistent performance  

---

### 🔹 3. PIR Sensor (Passive Infrared)  
  <img width="259" height="206" alt="image" src="https://github.com/user-attachments/assets/6f9c4c67-c1da-4242-ae43-5269ec67f511" />

- Detects motion based on infrared radiation emitted by objects  
- Sends digital HIGH/LOW signal to the microcontroller  
- Helps in identifying human presence near the door  
- Enhances system security by enabling motion-based detection  
- Low power consumption and cost-effective  
- Widely used in security and automation systems  

---

### 🔹 4. Jumper Wires  

- Male-to-Female
<img width="585" height="194" alt="image" src="https://github.com/user-attachments/assets/50f949e9-9eb2-4f66-a11a-76923fcd95a4" />

- Female-to-Female
<img width="529" height="211" alt="image" src="https://github.com/user-attachments/assets/452a1cd0-6098-4d2b-82c3-d2091b0a867c" />

- Used for electrical connections between components
- Ensures proper signal and power transmission  
- Types:
  - Male-to-Female  
  - Female-to-Female  
- Essential for prototyping and circuit assembly  
- Flexible and reusable for different configurations  

---

### 🔹 5. USB Cable  
 <img width="233" height="257" alt="image" src="https://github.com/user-attachments/assets/aaafe52e-4108-4b18-b375-e9d7a5eadd46" />


- Used to power the Raspberry Pi Pico  
- Enables code uploading from computer to microcontroller  
- Supports data communication during development and debugging  
- Provides stable power input during testing and operation  

---

### 🔹 6. Physical Structure
- Cardboard for the outer frame
 <img width="328" height="332" alt="image" src="https://github.com/user-attachments/assets/e5494db6-f062-41d6-9d77-3d5b81851567" />

- Glue and Scissors
 <img width="109" height="301" alt="image" src="https://github.com/user-attachments/assets/2240765c-0d7e-4d82-9eff-d0540722b200" />
<img width="25" height="25" alt="image" src="https://github.com/user-attachments/assets/369c8118-0ce5-4c58-990c-13991acf28f7" /> Before using scissors, read all instructions and ensure the blades are sharp and undamaged, as dull or broken scissors require excessive force and may slip
---

## ⚙️ Power Considerations

- Ensure stable and sufficient power supply for the servo motor  
- Avoid drawing excessive current directly from Pico GPIO pins  
- Use external power source if servo performance is inconsistent  
- Ensure proper grounding between all components  
- Prevent short circuits by verifying connections before powering  

---

## 🧠 Design Insight

- The system follows a modular hardware approach  
- Each component is independently replaceable and scalable  
- Integration of sensor + actuator enables real-time automation  
- Suitable for prototyping smart home security systems  

---

## 📌 Summary

The hardware setup forms the foundation of the system, enabling sensing, processing, communication, and actuation required for a functional smart door lock system. Proper selection and integration of components ensure reliability, efficiency, and scalability of the solution.
