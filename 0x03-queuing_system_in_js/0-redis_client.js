import { createClient } from 'redis';

const client = createClient();

client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

try {
  const con = client.connected;
  console.log('Redis client connected to the server');
} catch (err) {
  console.log(`Redis client not connected to the server: ${err}`);
}
