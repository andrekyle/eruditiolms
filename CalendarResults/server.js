const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3002;

// Set EJS as the view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Copy image files to public/images and overwrite stale files
const copyImagesToPublic = () => {
  const imageFiles = [
    'ai_bar_chart.png', 'ai_comparison.png', 'ai_histogram.png', 'ai_pie_chart.png',
    'azure_bar_chart.png', 'azure_comparison.png', 'azure_histogram.png', 'azure_pie_chart.png',
    'bar_chart.png', 'bar_chart_first_attempt.png', 'box_plot.png', 'box_plot_first_attempt.png',
    'comparison_retake.png', 'histogram.png', 'histogram_first_attempt.png', 'pie_chart.png', 'pie_chart_first_attempt.png'
  ];
  
  const publicImagesDir = path.join(__dirname, 'public', 'images');
  
  // Create the public/images directory if it doesn't exist
  if (!fs.existsSync(publicImagesDir)) {
    fs.mkdirSync(publicImagesDir, { recursive: true });
  }
  
  // Copy each image file to public/images, replacing old versions
  imageFiles.forEach(file => {
    const sourcePath = path.join(__dirname, file);
    const destPath = path.join(publicImagesDir, file);
    
    if (fs.existsSync(sourcePath)) {
      try {
        fs.copyFileSync(sourcePath, destPath);
        console.log(`Synced ${file} to public/images`);
      } catch (err) {
        console.error(`Error copying ${file}: ${err.message}`);
      }
    }
  });
};

// Copy images to public folder on server start
copyImagesToPublic();

// Routes
app.get('/', (req, res) => {
  res.render('index', {
    title: 'Exam Results Dashboard',
    year: '2024-2025'
  });
});

app.get('/python-report', (req, res) => {
  res.render('python_report', {
    title: 'Python Certification Report'
  });
});

app.get('/java-report', (req, res) => {
  res.render('java_report', {
    title: 'Java Certification Report'
  });
});

app.get('/ai-report', (req, res) => {
  res.render('ai_report', {
    title: 'Microsoft Azure AI-900 Fundamentals Exam Results'
  });
});

app.get('/azure-report', (req, res) => {
  res.render('azure_report', {
    title: 'Azure Certification Report'
  });
});

app.get('/powerbi-report', (req, res) => {
  res.render('powerbi_report', {
    title: 'Power BI Certification Report'
  });
});

app.get('/calendar', (req, res) => {
  res.render('calendar', {
    title: 'Academic Calendar 2025'
  });
});

app.get('/curriculum', (req, res) => {
  res.render('curriculum', {
    title: 'Curriculum 2025'
  });
});

// Handle original HTML file routes for compatibility
app.get('/python_report.html', (req, res) => {
  res.redirect('/python-report');
});

app.get('/java_report.html', (req, res) => {
  res.redirect('/java-report');
});

app.get('/ai_report.html', (req, res) => {
  res.redirect('/ai-report');
});

app.get('/azure_report.html', (req, res) => {
  res.redirect('/azure-report');
});

app.get('/powerbi_report.html', (req, res) => {
  res.redirect('/powerbi-report');
});

app.get('/calendar_2025.html', (req, res) => {
  res.redirect('/calendar');
});

app.get('/curriculum_2025.html', (req, res) => {
  res.redirect('/curriculum');
});

app.get('/index.html', (req, res) => {
  res.redirect('/');
});

// API endpoints for chart data
app.get('/api/chart-data', (req, res) => {
  const chartData = {
    certifications: 352,
    passRate: 93,
    retakeSuccess: 85,
    topPerformers: 35
  };
  res.json(chartData);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
