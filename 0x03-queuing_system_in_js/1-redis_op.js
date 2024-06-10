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

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, data) => {
    if (err) err;
    if (data) console.log(data);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
