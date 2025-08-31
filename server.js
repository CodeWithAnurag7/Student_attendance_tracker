const express = require("express");
const path = require("path");
const app = express();

// Add CORS headers to allow requests from browsers
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.use(express.json());

app.use(express.static(path.join(__dirname, "template")));

let students = [];
let attendance = [];

app.post("/students", (req, res) => {
  try {
    const { id, name } = req.body;

    if (!id || !name) {
      return res.status(400).json({ error: "Student ID and name are required" });
    }

    if (students.some(student => student.id === id)) {
      return res.status(409).json({ error: "Student ID already exists" });
    }

    students.push({ id, name });
    res.status(201).json({ message: "Student added successfully", students });
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
});

app.get("/students", (req, res) => {
  try {
    res.json(students);
  } catch (error) {
    res.status(500).json({ error: "Failed to retrieve students" });
  }
});

app.post("/attendance", (req, res) => {
  try {
    const { studentId, date, status } = req.body;

    if (!studentId || !date || !status) {
      return res.status(400).json({ error: "Student ID, date, and status are required" });
    }

    if (!students.some(student => student.id === studentId)) {
      return res.status(404).json({ error: "Student not found" });
    }

    const existingIndex = attendance.findIndex(a => a.studentId === studentId && a.date === date);
    
    if (existingIndex >= 0) {
      attendance[existingIndex].status = status;
      res.json({ message: "Attendance updated", attendance });
    } else {
      attendance.push({ studentId, date, status });
      res.status(201).json({ message: "Attendance marked", attendance });
    }
  } catch (error) {
    res.status(500).json({ error: "Failed to mark attendance" });
  }
});

app.get("/attendance/:studentId", (req, res) => {
  try {
    const { studentId } = req.params;
    const records = attendance.filter(a => a.studentId === studentId);
    
    if (records.length === 0) {
      return res.status(404).json({ error: "No attendance records found for this student" });
    }
    
    res.json(records);
  } catch (error) {
    res.status(500).json({ error: "Failed to retrieve attendance records" });
  }
});

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "template", "server.html"));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});