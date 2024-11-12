# Grain Storage Monitoring System  

## Project Overview  

Grain spoilage during storage poses a significant challenge to the agriculture industry, leading to substantial losses. Traditional monitoring methods often lack real-time insights and the ability to predict potential spoilage issues. This project proposes an **AI-powered Grain Storage Monitoring System** that combines advanced sensor technologies, machine learning algorithms, and a cloud-based platform to ensure optimal storage conditions and minimize grain loss.  

### Key Features:  
- **Real-time Monitoring**: Tracks temperature, humidity, acoustic emissions, and visual data.  
- **AI-based Analysis**: Uses machine learning models to detect pests, mold, and other spoilage indicators.  
- **User-friendly Interface**: Provides actionable insights through a web dashboard and mobile app.  
- **Proactive Alerts**: Notifies users of anomalies, enabling timely interventions.  
- **Data Visualization**: Displays historical trends for informed decision-making.  





## Proposed System Architecture  

### **1. Data Collection**  
- **Environmental Sensors**: Capture real-time data on temperature, humidity, and acoustics to assess grain health.  
- **NIR Sensors**: Detect spoilage indicators such as mold growth through near-infrared spectroscopy.  
- **High-Resolution Cameras**: Provide visual inspection capabilities for detecting pests and mold.  

### **2. Data Transmission**  
- **Wireless Gateway**: Collects and transmits sensor data to the cloud platform for processing and storage.  

### **3. Data Processing & Analytics**  
- **Cloud Platform**:  
  - Stores and processes sensor data securely.  
  - Deploys machine learning models for anomaly detection and quality assessment.  
  - Triggers real-time alerts when anomalies are detected.  
- **Machine Learning Models**:  
  - **YOLO, SSD, Faster R-CNN**: Object detection for pest and mold identification.  
  - **CNNs & SVMs**: Analyze sensor data to detect spoilage patterns.  
  - **Isolation Forests**: Identify anomalies in environmental data.  

### **4. User Interface**  
- **Mobile App & Web Dashboard**:  
  - Real-time monitoring of environmental parameters.  
  - Historical data visualization with interactive graphs and charts.  
  - Alerts and recommendations for proactive grain management.  

## Implementation Details  

### **Technologies Used**  
#### **Hardware**  
- **DHT11 Sensor**: Measures temperature and humidity.  
- **ESP8266 Wi-Fi Module**: Enables wireless communication.  
- **Arduino UNO R3**: Captures environmental data.  
- **MQ2 Sensor**: Detects gases like CO2, methane, and hydrogen.  

#### **Software**  
- **Front-end**: HTML, CSS, JavaScript  
- **Back-end**: Python (Flask), Node.js  
- **Database**: MongoDB, MySQL  
- **Version Control**: Git  

### **Machine Learning Algorithms**  
- **YOLO, RetinaNet**: For real-time object detection.  
- **Faster R-CNN, Mask R-CNN**: Balancing detection accuracy and speed.  
- **Transformers (DETR)**: End-to-end object detection using transformers.  



## Evaluation Parameters  

### **1. Accuracy of Detection**  
- **Precision & Recall**: Evaluate the system’s ability to detect true instances of spoilage and pests.  
- **F1 Score**: Balances precision and recall for uneven data distribution.  

### **2. Sensor Reliability**  
- **Sensor Accuracy & Calibration**: Ensures accurate readings.  
- **Failure Rate**: Monitors the robustness of sensors over time.  

### **3. Machine Learning Model Performance**  
- **Model Accuracy**: Effectiveness in identifying anomalies.  
- **Inference Time**: Real-time analysis capability.  

### **4. Real-Time Monitoring**  
- **Data Latency**: Measures delay between data capture and display.  
- **Transmission Rate**: Speed of data transfer to the cloud.  

### **5. User Experience**  
- **Ease of Use**: Intuitive interfaces for efficient monitoring.  
- **Alert Customization**: Adjustable thresholds for alerts.  



## Future Scope  

1. **Integration of Advanced Models**: Explore deep learning techniques like RNNs and LSTMs for improved analysis of time-series data.  
2. **Additional Sensors**: Include oxygen level and VOC sensors for comprehensive monitoring.  
3. **IoT-based Automation**: Automate responses like ventilation or pest control based on system alerts.  
4. **Predictive Maintenance**: Anticipate sensor or equipment failure for uninterrupted operations.  
5. **Multi-grain Support**: Optimize for different grain types and scale for larger facilities.  



## Contribution and Usage  

This project is designed to revolutionize grain storage by providing farmers and facility managers with the tools they need to monitor and maintain optimal storage conditions efficiently. Users can install the system on their facilities and use the web or mobile interface for seamless monitoring and management.  

### **Getting Started**  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/username/grain-storage-monitoring.git  
   ```  
2. Follow the instructions in the `README.md` to set up the environment and deploy the application.

![image](https://github.com/user-attachments/assets/04fe9587-503d-458e-b610-826b2f3203f5)

![image](https://github.com/user-attachments/assets/76311929-36ef-40a8-a451-c07f4e2180f4)

![image](https://github.com/user-attachments/assets/91ef3c7d-3f4d-40f8-958b-ae6b6e636ee0)

![image](https://github.com/user-attachments/assets/edc1dc13-0ae5-4c9a-b315-bd0f8033a1a4)

![image](https://github.com/user-attachments/assets/24d13b9a-4cff-4ba9-89bf-3455ad8deded)

![image](https://github.com/user-attachments/assets/e746051f-e690-472f-9fd0-d4ec21a41e9c)

![image](https://github.com/user-attachments/assets/aaa7057c-5d3a-4aa5-abdf-302977eb3cbd)







  



