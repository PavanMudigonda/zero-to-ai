const { MongoClient } = require('mongodb');

const mongoUrl = "mongodb://admin:password@localhost:27017?authSource=admin";

console.log('Attempting to connect to MongoDB...');
console.log('URL:', mongoUrl);

const options = {
    serverSelectionTimeoutMS: 5000,  // Timeout after 5 seconds
    connectTimeoutMS: 10000,
};

async function testConnection() {
    let client;
    try {
        console.log('Creating MongoClient...');
        client = new MongoClient(mongoUrl, options);
        
        console.log('Connecting...');
        await client.connect();
        
        console.log('✅ Successfully connected to MongoDB!');
        
        const db = client.db('user-account');
        console.log('Querying database...');
        
        const result = await db.collection('users').findOne({ userid: 1 });
        
        console.log('✅ Query successful!');
        console.log('Result:', result || 'No user found (empty database)');
        
    } catch (err) {
        console.error('❌ Error:', err.message);
        console.error('Error code:', err.code);
        console.error('Full error:', err);
    } finally {
        if (client) {
            await client.close();
            console.log('Connection closed.');
        }
        process.exit(0);
    }
}

testConnection();
