# ⚙️ Runtime Working — Smart Door Lock System

## 📌 Overview

This document explains the **runtime behavior** of the Smart Door Lock System — how the system operates step-by-step after execution begins.

Unlike architecture, this focuses on **execution flow, timing, and system response**.

---

## 🚀 Execution Timeline

### 🟢 Phase 1: Boot & Initialization

- Power is supplied to Raspberry Pi Pico
- MicroPython script (`main.py`) starts executing
- Hardware components are initialized:
  - Servo motor set to default (locked position)
  - PIR sensor configured as input
- System prepares for network connection

---

### 🔵 Phase 2: Network Establishment

- Pico activates WiFi interface
- Attempts connection using SSID and password
- Waits until connection is successful
- Prints assigned IP address

👉 This IP becomes the system access point

---

### 🟡 Phase 3: Server Startup

- Socket server is created
- Bound to IP address and port 80
- System enters **listening mode**

👉 At this point, system is idle but ready

---

### 🟣 Phase 4: Idle Monitoring State

System continuously performs two tasks:

1. Waits for incoming HTTP requests  
2. Monitors PIR sensor input  

👉 This is a **non-blocking continuous loop**

---

### 🔴 Phase 5: Request Trigger Event

When a user interacts:

#### Case A: `/DoorOpen`
- HTTP request received
- Request parsed from client data
- Condition matched
- Servo motor rotates to unlock position
- Internal state updated → `"Open"`

---

#### Case B: `/DoorClose`
- HTTP request received
- Request parsed
- Servo returns to lock position
- Internal state updated → `"Closed"`

---

### 🟠 Phase 6: Sensor Trigger Event

- PIR sensor detects motion
- Output signal goes HIGH
- Pico reads input using GPIO

Possible actions:
- Log message: “Motion Detected”
- Trigger automation (future scope)

---

### ⚪ Phase 7: Response Handling

- HTML response is generated dynamically
- `{state}` is replaced with current status
- Response sent back to client browser
- Connection is closed

---

## 🔁 Continuous Runtime Loop

The system operates in an infinite loop:
Wait → Detect → Process → Respond → Repeat
👉 No termination unless manually stopped

---

## 🧠 Internal Decision Logic

| Condition | Action |
|----------|--------|
| `/DoorOpen` | Servo → Unlock |
| `/DoorClose` | Servo → Lock |
| PIR = HIGH | Motion detected |
| No input | Stay idle |

---

## ⏱️ Real-Time Behavior

- Response time depends on:
  - Network latency
  - Processing speed of Pico
- Typically near-instant within local network

---

## ⚠️ Runtime Constraints

- Single-threaded execution  
- Handles one request at a time  
- Limited memory (microcontroller environment)  

---

## 🔮 Runtime Improvements

- Add asynchronous request handling  
- Introduce interrupt-based sensor detection  
- Implement auto-lock timer  
- Add authentication before command execution  

---

## 📌 Summary

The system operates as a **real-time event-driven embedded application**, continuously monitoring inputs and responding to user commands with minimal delay.
