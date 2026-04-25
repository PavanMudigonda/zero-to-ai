let express = require('express');
let path = require('path');
let fs = require('fs');
let MongoClient = require('mongodb').MongoClient;
let bodyParser = require('body-parser');
let app = express();

app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());

// Add CORS headers
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname, "index.html"));
  });

app.get('/profile-picture', function (req, res) {
  let img = fs.readFileSync(path.join(__dirname, "images/profile-1.jpg"));
  res.writeHead(200, {'Content-Type': 'image/jpg' });
  res.end(img, 'binary');
});

// Health check endpoint
app.get('/health', function (req, res) {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// use when starting application locally
let mongoUrlLocal = "mongodb://admin:password@localhost:27017?authSource=admin";

// use when starting application as docker container
let mongoUrlDocker = "mongodb://admin:password@mongodb?authSource=admin";

// Auto-detect environment and select MongoDB URL
// If MONGO_DB_USERNAME env var exists, we're running in Docker
let mongoUrl = process.env.MONGO_DB_USERNAME ? mongoUrlDocker : mongoUrlLocal;

console.log('MongoDB URL:', mongoUrl.replace(/password@/, '***@')); // Log URL without exposing password

// MongoDB connection options (no longer needed in driver v4.0+)
let mongoClientOptions = {
  serverSelectionTimeoutMS: 5000,
  connectTimeoutMS: 10000
};

// "user-account" in demo with docker. "my-db" in demo with docker-compose
let databaseName = "user-account";

app.post('/update-profile', async function (req, res) {
  let client;
  try {
    const userObj = req.body;
    userObj['userid'] = 1;

    client = await MongoClient.connect(mongoUrl, mongoClientOptions);
    const db = client.db(databaseName);
    
    const myquery = { userid: 1 };
    const newvalues = { $set: userObj };

    await db.collection("users").updateOne(myquery, newvalues, {upsert: true});
    
    // Send response
    res.send(userObj);
  } catch (err) {
    console.error('MongoDB error:', err);
    res.status(500).send({ error: 'Database operation failed', details: err.message });
  } finally {
    if (client) {
      await client.close();
    }
  }
});

app.get('/get-profile', async function (req, res) {
  let client;
  try {
    // Connect to the db
    client = await MongoClient.connect(mongoUrl, mongoClientOptions);
    const db = client.db(databaseName);
    
    const result = await db.collection("users").findOne({ userid: 1 });
    
    // Send response
    res.send(result ? result : {});
  } catch (err) {
    console.error('MongoDB error:', err);
    res.status(500).send({ error: 'Database operation failed', details: err.message });
  } finally {
    if (client) {
      await client.close();
    }
  }
});

app.listen(3000, function () {
  console.log("app listening on port 3000!");
});
