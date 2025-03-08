# 🌡️ MQTT Weather Station Dashboard

A modern real-time weather monitoring system that collects temperature and humidity data from an MQTT broker, stores it in SQLite, and provides beautiful visualizations with live updates.

## ✨ Features

- 📊 Real-time temperature and humidity monitoring with smooth animations
- 📈 Interactive charts with historical data visualization
- 🔄 Automatic 5-minute averaging system
- 💾 Persistent SQLite database storage
- 📱 Fully responsive design for all devices
- ⚡ Live updates with WebSocket connection
- 🎨 Modern, clean UI with dynamic themes

## 🚀 Quick Start

### Prerequisites

- Node.js (v14 or later)
- npm (v6 or later)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mahingaRodin/mqtt-weather-app.git
   cd mqtt-weather-app
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Set up the public directory:

   ```bash
   mkdir -p public
   cp index.html public/
   ```

4. Launch the application:

   ```bash
   node server.js
   ```

5. View the dashboard:
   Open your browser and visit `http://localhost:3000`

## 🏗️ Project Structure

```
mqtt-weather-app/
├── 📁 public/
│   └── 📄 index.html      # Frontend dashboard interface
├── 📄 server.js           # Express backend & API endpoints
├── 📄 package.json        # Project dependencies
├── 📄 weather_data.db     # SQLite database (auto-generated)
└── 📄 README.md           # Documentation
```

## 🔧 How It Works

1. **Data Collection**: Frontend establishes WebSocket connection to MQTT broker
2. **Real-time Updates**: Live temperature and humidity values with smooth animations
3. **Data Storage**: Each reading is stored in SQLite via the backend API
4. **Data Processing**: 5-minute averages are automatically calculated and stored
5. **Visualization**: Interactive charts display historical trends and live updates

## 🔌 API Endpoints

| Endpoint               | Method | Description               |
| ---------------------- | ------ | ------------------------- |
| `/api/weather/data`    | POST   | Store new sensor readings |
| `/api/weather/current` | GET    | Get latest readings       |
| `/api/weather/history` | GET    | Retrieve historical data  |

## 📊 Database Schema

### Raw Readings Table

```sql
CREATE TABLE raw_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,        -- 'temperature' or 'humidity'
    value REAL NOT NULL,       -- Sensor reading
    timestamp TEXT NOT NULL    -- ISO timestamp
);
```

### Averaged Data Table

```sql
CREATE TABLE avg_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    avg_temperature REAL,      -- 5-minute temperature average
    avg_humidity REAL,         -- 5-minute humidity average
    timestamp TEXT NOT NULL    -- ISO timestamp
);
```

## 🚀 Running the Application

1. Navigate to the project directory
2. Start the server:
   ```bash
   node server.js
   ```
3. Access the dashboard at `http://localhost:3000`

## 👨‍💻 Developer

Created by [mahingaRodin](https://github.com/mahingaRodin)

## 📝 License

This project is open source and available under the MIT License.

---

<div align="center">
Made with ❤️ by mahingaRodin
</div>
