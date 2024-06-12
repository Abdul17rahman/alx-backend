import { createClient, print } from 'redis';

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

const Holberton = {
  "Portland": 50,
  "Seattle": 80,
  "Bogota": 20,
  "Cali": 40,
  "Paris": 2
}

for (const val in Holberton) {
  const value = Holberton[val].toString()
  client.hset('Holberton', val, value, (err, res) => {
    if (err) err
    print
  })
}

console.log(client.hgetall('Holberton'))


