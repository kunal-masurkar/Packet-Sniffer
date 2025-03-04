# Packet Sniffer

## 📌 Overview
A **Network Packet Sniffer** that captures and analyzes network packets in real-time using **Scapy** in Python. This tool allows users to inspect network traffic, providing useful insights for **network monitoring, security analysis, and debugging**.

## 🚀 Features
- Captures real-time network packets
- Displays packet details (IP, Protocol, etc.)
- Lightweight and easy to use
- Works on Windows, Linux, and macOS

## 📦 Requirements
Before running the script, install the dependencies:

### 🔹 Install Required Modules
```sh
pip install -r requirements.txt
```

### 🔹 Install **Npcap** (Windows Users)
If you're on **Windows**, install **Npcap** for packet sniffing:
1. Download from [Npcap Official Site](https://nmap.org/npcap/)
2. During installation, **check "Install Npcap in WinPcap API-compatible Mode"**

## 🔧 How to Run
1. **Run the script as Administrator** (Windows) or **use sudo** (Linux/macOS):
   ```sh
   python sniffer.py
   ```
2. The tool will start capturing packets and displaying details in real-time.

## 🔹 Notes
- **Run as administrator/root** for proper packet capturing.
- Works better on **Linux/macOS** due to native packet capturing support.
- Modify `packet_callback()` to filter specific packets.

📌 **Use responsibly!** Unauthorized sniffing may violate security policies. 🚀

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

## 💡 Author
👨‍💻 Developed by **Kunal Masurkar**  
🌐 [GitHub](https://github.com/kunal-masurkar) | 🔗 [LinkedIn](https://linkedin.com/in/kunal-masurkar-8494a123a)
